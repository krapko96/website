import plotly.express as px


def render():
    data = {
        "Category": [
            "Sports", "Politics", "Crypto", "Finance",
            "Weather", "Entertainment", "Economics", "Science",
        ],
        "Volume ($B)": [13.18, 2.45, 0.84, 0.76, 0.30, 0.22, 0.18, 0.07],
    }
    fig = px.treemap(
        data,
        path=["Category"],
        values="Volume ($B)",
        color="Volume ($B)",
        color_continuous_scale=["#1a1a2e", "#4285f4", "#34a853"],
        title="Kalshi: Total Notional Volume by Category",
    )
    fig.update_layout(
        margin=dict(t=40, l=0, r=0, b=0),
        font_family="IBM Plex Mono, monospace",
        paper_bgcolor="rgba(0,0,0,0)",
        coloraxis_showscale=False,
    )
    fig.update_traces(
        textinfo="label+value",
        texttemplate="<b>%{label}</b><br>$%{value:.2f}B",
        textfont_size=14,
    )
    return fig.to_html(include_plotlyjs="cdn", full_html=False)
