import numpy as np
import pandas as pd
import plotly.express as px
import streamlit as st


st.set_page_config(
    page_title="Dashboard Performa Penjualan",
    page_icon="📊",
    layout="wide",
)


@st.cache_data
def generate_data() -> pd.DataFrame:
    """Create a repeatable synthetic dataset for local dashboard use."""
    rng = np.random.default_rng(42)
    dates = pd.date_range(start="2026-01-01", periods=180, freq="D")
    categories = ["Elektronik", "Pakaian", "Makanan & Minuman", "Buku"]
    regions = ["Jakarta", "Bengkulu", "Bandung", "Surabaya"]
    statuses = ["Selesai", "Pending", "Gagal"]

    return pd.DataFrame(
        {
            "Tanggal": rng.choice(dates, size=1000),
            "Wilayah": rng.choice(regions, size=1000),
            "Kategori": rng.choice(categories, size=1000),
            "Penjualan": rng.integers(50, 2000, size=1000) * 1000,
            "Status": rng.choice(statuses, size=1000, p=[0.8, 0.15, 0.05]),
        }
    ).assign(
        Profit=lambda data: (
            data["Penjualan"] * rng.uniform(0.1, 0.35, size=len(data))
        ).astype(int)
    )


def format_rupiah(value: int) -> str:
    return f"Rp {value:,.0f}".replace(",", ".")


df_raw = generate_data()

st.title("📊 Dashboard Performa Penjualan Interaktif")
st.caption(
    "Pantau ringkasan bisnis, saring data, lalu telusuri transaksi saat dibutuhkan."
)

st.sidebar.header("🔍 Filter Data")
selected_regions = st.sidebar.multiselect(
    "Wilayah",
    options=sorted(df_raw["Wilayah"].unique()),
    default=sorted(df_raw["Wilayah"].unique()),
)
selected_categories = st.sidebar.multiselect(
    "Kategori produk",
    options=sorted(df_raw["Kategori"].unique()),
    default=sorted(df_raw["Kategori"].unique()),
)

filtered_df = df_raw[
    df_raw["Wilayah"].isin(selected_regions)
    & df_raw["Kategori"].isin(selected_categories)
]

st.subheader("📌 Ringkasan Eksekutif")
total_sales = int(filtered_df["Penjualan"].sum())
total_profit = int(filtered_df["Profit"].sum())
transaction_count = len(filtered_df)
failed_count = int(filtered_df["Status"].eq("Gagal").sum())

kpi_columns = st.columns(4)
kpi_columns[0].metric("Total Penjualan", format_rupiah(total_sales))
kpi_columns[1].metric("Total Profit", format_rupiah(total_profit))
kpi_columns[2].metric("Total Transaksi", f"{transaction_count:,}".replace(",", "."))
kpi_columns[3].metric("Transaksi Gagal", f"{failed_count:,}".replace(",", "."))

st.divider()

if filtered_df.empty:
    st.info("Tidak ada transaksi untuk filter yang dipilih. Pilih wilayah atau kategori lain.")
else:
    chart_columns = st.columns(2)

    with chart_columns[0]:
        st.subheader("📈 Tren Penjualan Harian")
        daily_sales = (
            filtered_df.groupby("Tanggal", as_index=False)["Penjualan"]
            .sum()
            .sort_values("Tanggal")
        )
        line_chart = px.line(
            daily_sales,
            x="Tanggal",
            y="Penjualan",
            labels={"Penjualan": "Penjualan (Rp)", "Tanggal": "Tanggal"},
            template="plotly_white",
        )
        line_chart.update_traces(
            line_color="#2563eb",
            line_width=2,
            hovertemplate="%{x|%d %b %Y}<br>Penjualan: Rp %{y:,.0f}<extra></extra>",
        )
        line_chart.update_layout(
            margin=dict(l=10, r=10, t=20, b=10),
            showlegend=False,
            yaxis=dict(tickformat=",.0f", showgrid=False, rangemode="tozero"),
            xaxis=dict(showgrid=False),
        )
        st.plotly_chart(line_chart, use_container_width=True)

    with chart_columns[1]:
        st.subheader("📊 Penjualan per Kategori")
        category_sales = (
            filtered_df.groupby("Kategori", as_index=False)["Penjualan"]
            .sum()
            .sort_values("Penjualan", ascending=False)
        )
        bar_chart = px.bar(
            category_sales,
            x="Kategori",
            y="Penjualan",
            color="Kategori",
            color_discrete_sequence=px.colors.qualitative.Safe,
            labels={"Penjualan": "Penjualan (Rp)", "Kategori": "Kategori"},
            template="plotly_white",
        )
        bar_chart.update_traces(
            hovertemplate="%{x}<br>Penjualan: Rp %{y:,.0f}<extra></extra>"
        )
        bar_chart.update_layout(
            margin=dict(l=10, r=10, t=20, b=10),
            showlegend=False,
            yaxis=dict(tickformat=",.0f", showgrid=False, rangemode="tozero"),
            xaxis=dict(showgrid=False),
        )
        st.plotly_chart(bar_chart, use_container_width=True)

with st.expander("📄 Tampilkan detail transaksi"):
    st.caption("Gunakan filter di sidebar untuk mempersempit data transaksi.")
    st.dataframe(
        filtered_df.sort_values("Tanggal", ascending=False),
        use_container_width=True,
        hide_index=True,
    )

st.caption(
    "Prototipe data sintetis untuk tugas HCI & Data Visualization "
    "— Program Studi Informatika, Universitas Bengkulu."
)
