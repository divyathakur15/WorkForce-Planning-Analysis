"""
Professional Chart Components for Workforce Planning Dashboard
"""

import plotly.graph_objects as go
import plotly.express as px
from dashboard_config import COLORS, FONTS, CHART_CONFIG

def create_bar_chart(data, x_col, y_col, title, color=None, horizontal=False):
    """Create a professional bar chart"""
    
    if color is None:
        color = COLORS['primary']
    
    if horizontal:
        fig = go.Figure(go.Bar(
            x=data[y_col],
            y=data[x_col],
            orientation='h',
            marker=dict(color=color),
            text=data[y_col],
            textposition='auto'
        ))
    else:
        fig = go.Figure(go.Bar(
            x=data[x_col],
            y=data[y_col],
            marker=dict(color=color),
            text=data[y_col],
            textposition='auto'
        ))
    
    fig.update_layout(
        title=dict(text=title, font=dict(size=16, color=COLORS['dark'])),
        **CHART_CONFIG,
        margin=dict(t=50, b=40, l=50, r=30),
        height=350
    )
    
    return fig


def create_line_chart(data, x_col, y_col, title, color=None, show_markers=True):
    """Create a professional line chart"""
    
    if color is None:
        color = COLORS['primary']
    
    mode = 'lines+markers' if show_markers else 'lines'
    
    fig = go.Figure(go.Scatter(
        x=data[x_col],
        y=data[y_col],
        mode=mode,
        line=dict(color=color, width=3),
        marker=dict(size=8, color=color)
    ))
    
    fig.update_layout(
        title=dict(text=title, font=dict(size=16, color=COLORS['dark'])),
        **CHART_CONFIG,
        margin=dict(t=50, b=40, l=50, r=30),
        height=350
    )
    
    return fig


def create_pie_chart(data, values_col, names_col, title, colors=None):
    """Create a professional pie chart"""
    
    if colors is None:
        colors = COLORS['chart_colors']
    
    fig = go.Figure(go.Pie(
        values=data[values_col],
        labels=data[names_col],
        hole=0,
        marker=dict(colors=colors, line=dict(color='white', width=2)),
        textinfo='label+percent',
        textposition='auto'
    ))
    
    fig.update_layout(
        title=dict(text=title, font=dict(size=16, color=COLORS['dark'])),
        **CHART_CONFIG,
        margin=dict(t=50, b=30, l=30, r=30),
        height=350,
        showlegend=True,
        legend=dict(
            orientation="v",
            yanchor="middle",
            y=0.5,
            xanchor="left",
            x=1.02,
            font=dict(size=11)
        )
    )
    
    return fig


def create_donut_chart(data, values_col, names_col, title, colors=None):
    """Create a professional donut chart"""
    
    if colors is None:
        colors = COLORS['chart_colors']
    
    fig = go.Figure(go.Pie(
        values=data[values_col],
        labels=data[names_col],
        hole=0.4,
        marker=dict(colors=colors, line=dict(color='white', width=2)),
        textinfo='label+percent',
        textposition='auto'
    ))
    
    fig.update_layout(
        title=dict(text=title, font=dict(size=16, color=COLORS['dark'])),
        **CHART_CONFIG,
        margin=dict(t=50, b=30, l=30, r=30),
        height=350,
        showlegend=True,
        legend=dict(
            orientation="v",
            yanchor="middle",
            y=0.5,
            xanchor="left",
            x=1.02,
            font=dict(size=11)
        )
    )
    
    return fig


def create_stacked_bar_chart(data, x_col, y_cols, title, colors=None):
    """Create a professional stacked bar chart"""
    
    if colors is None:
        colors = COLORS['chart_colors']
    
    fig = go.Figure()
    
    for i, col in enumerate(y_cols):
        fig.add_trace(go.Bar(
            x=data[x_col],
            y=data[col],
            name=col,
            marker=dict(color=colors[i % len(colors)])
        ))
    
    fig.update_layout(
        title=title,
        barmode='stack',
        **CHART_CONFIG,
        margin=dict(t=60, b=60, l=60, r=40),
        height=400,
        legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.02,
            xanchor="right",
            x=1
        )
    )
    
    return fig


def create_grouped_bar_chart(data, x_col, y_cols, title, colors=None):
    """Create a professional grouped bar chart"""
    
    if colors is None:
        colors = COLORS['chart_colors']
    
    fig = go.Figure()
    
    for i, col in enumerate(y_cols):
        fig.add_trace(go.Bar(
            x=data[x_col],
            y=data[col],
            name=col,
            marker=dict(color=colors[i % len(colors)])
        ))
    
    fig.update_layout(
        title=title,
        barmode='group',
        **CHART_CONFIG,
        margin=dict(t=60, b=60, l=60, r=40),
        height=400,
        legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.02,
            xanchor="right",
            x=1
        )
    )
    
    return fig


def create_heatmap(data, x_col, y_col, z_col, title, colorscale='Blues'):
    """Create a professional heatmap"""
    
    # Pivot data for heatmap
    pivot_data = data.pivot_table(values=z_col, index=y_col, columns=x_col, aggfunc='mean')
    
    fig = go.Figure(go.Heatmap(
        z=pivot_data.values,
        x=pivot_data.columns,
        y=pivot_data.index,
        colorscale=colorscale,
        text=pivot_data.values,
        texttemplate='%{text:.1f}',
        textfont={"size": 10},
        colorbar=dict(title=z_col)
    ))
    
    fig.update_layout(
        title=title,
        **CHART_CONFIG,
        margin=dict(t=60, b=60, l=120, r=40),
        height=400
    )
    
    return fig


def create_gauge_chart(value, title, min_val=0, max_val=100, threshold_low=30, 
                       threshold_high=70):
    """Create a professional gauge chart"""
    
    # Determine color based on thresholds
    if value < threshold_low:
        color = COLORS['danger']
    elif value < threshold_high:
        color = COLORS['warning']
    else:
        color = COLORS['success']
    
    fig = go.Figure(go.Indicator(
        mode="gauge+number+delta",
        value=value,
        title={'text': title, 'font': {'size': 20}},
        delta={'reference': (threshold_low + threshold_high) / 2},
        gauge={
            'axis': {'range': [min_val, max_val], 'tickwidth': 1},
            'bar': {'color': color},
            'steps': [
                {'range': [min_val, threshold_low], 'color': 'rgba(239, 68, 68, 0.2)'},
                {'range': [threshold_low, threshold_high], 'color': 'rgba(245, 158, 11, 0.2)'},
                {'range': [threshold_high, max_val], 'color': 'rgba(16, 185, 129, 0.2)'}
            ],
            'threshold': {
                'line': {'color': COLORS['dark'], 'width': 4},
                'thickness': 0.75,
                'value': value
            }
        }
    ))
    
    fig.update_layout(
        **CHART_CONFIG,
        margin=dict(t=50, b=30, l=30, r=30),
        height=280
    )
    
    return fig


def create_multi_line_chart(data, x_col, y_cols, title, colors=None):
    """Create a professional multi-line chart"""
    
    if colors is None:
        colors = COLORS['chart_colors']
    
    fig = go.Figure()
    
    for i, col in enumerate(y_cols):
        fig.add_trace(go.Scatter(
            x=data[x_col],
            y=data[col],
            mode='lines+markers',
            name=col,
            line=dict(color=colors[i % len(colors)], width=3),
            marker=dict(size=8)
        ))
    
    fig.update_layout(
        title=title,
        **CHART_CONFIG,
        margin=dict(t=60, b=60, l=60, r=40),
        height=400,
        legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.02,
            xanchor="right",
            x=1
        )
    )
    
    return fig


def create_scatter_plot(data, x_col, y_col, title, color_col=None, size_col=None):
    """Create a professional scatter plot"""
    
    if color_col:
        fig = px.scatter(
            data, 
            x=x_col, 
            y=y_col,
            color=color_col,
            size=size_col,
            color_discrete_sequence=COLORS['chart_colors'],
            title=title
        )
    else:
        fig = go.Figure(go.Scatter(
            x=data[x_col],
            y=data[y_col],
            mode='markers',
            marker=dict(
                size=10 if size_col is None else data[size_col],
                color=COLORS['primary'],
                opacity=0.6
            )
        ))
        fig.update_layout(title=title)
    
    fig.update_layout(
        **CHART_CONFIG,
        margin=dict(t=60, b=60, l=60, r=40),
        height=400
    )
    
    return fig


def create_histogram(data, x_col, title, nbins=30, color=None):
    """Create a professional histogram"""
    
    if color is None:
        color = COLORS['primary']
    
    fig = go.Figure(go.Histogram(
        x=data[x_col],
        nbinsx=nbins,
        marker=dict(color=color, line=dict(color='white', width=1))
    ))
    
    fig.update_layout(
        title=title,
        **CHART_CONFIG,
        margin=dict(t=60, b=60, l=60, r=40),
        height=400,
        xaxis_title=x_col,
        yaxis_title='Count'
    )
    
    return fig


def create_box_plot(data, x_col, y_col, title, color=None):
    """Create a professional box plot"""
    
    if color is None:
        color = COLORS['primary']
    
    fig = go.Figure(go.Box(
        x=data[x_col],
        y=data[y_col],
        marker=dict(color=color),
        boxmean='sd'
    ))
    
    fig.update_layout(
        title=title,
        **CHART_CONFIG,
        margin=dict(t=60, b=60, l=60, r=40),
        height=400
    )
    
    return fig
