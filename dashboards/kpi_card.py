"""
Professional KPI Card Components for Workforce Planning Dashboard
"""

import plotly.graph_objects as go
from dashboard_config import COLORS, FONTS, KPI_TEMPLATES

def create_kpi_card(value, label, icon='📊', trend=None, trend_direction='up', 
                    color=None, format_string='{:,.0f}'):
    """
    Create a professional KPI card with optional trend indicator
    
    Parameters:
    - value: The KPI value to display
    - label: Label for the KPI
    - icon: Emoji or icon to display
    - trend: Trend value (e.g., +5.2, -3.1)
    - trend_direction: 'up', 'down', or 'neutral'
    - color: Card accent color
    - format_string: Format string for the value
    """
    
    if color is None:
        color = COLORS['primary']
    
    # Format the value
    if isinstance(format_string, str) and '{}' in format_string:
        formatted_value = format_string.format(value)
    else:
        formatted_value = f"{value:,.0f}"
    
    # Determine trend color and arrow
    if trend is not None:
        if trend_direction == 'up':
            trend_color = COLORS['success'] if trend > 0 else COLORS['danger']
            trend_arrow = '↑' if trend > 0 else '↓'
        elif trend_direction == 'down':
            trend_color = COLORS['danger'] if trend > 0 else COLORS['success']
            trend_arrow = '↑' if trend > 0 else '↓'
        else:
            trend_color = COLORS['medium']
            trend_arrow = '→'
        
        trend_text = f"{trend_arrow} {abs(trend):.1f}%"
    else:
        trend_text = ""
        trend_color = COLORS['medium']
    
    # Create the KPI card as a plotly figure
    fig = go.Figure()
    
    # Add invisible trace (for sizing)
    fig.add_trace(go.Scatter(
        x=[0, 1],
        y=[0, 1],
        mode='markers',
        marker=dict(size=0, opacity=0),
        showlegend=False
    ))
    
    # Add icon
    fig.add_annotation(
        x=0.1, y=0.85,
        text=icon,
        font=dict(size=40),
        showarrow=False,
        xanchor='left'
    )
    
    # Add value
    fig.add_annotation(
        x=0.5, y=0.55,
        text=formatted_value,
        font=dict(
            family=FONTS['kpi_value']['family'],
            size=FONTS['kpi_value']['size'],
            color=color
        ),
        showarrow=False,
        xanchor='center'
    )
    
    # Add label
    fig.add_annotation(
        x=0.5, y=0.25,
        text=label,
        font=dict(
            family=FONTS['kpi_label']['family'],
            size=FONTS['kpi_label']['size'],
            color=COLORS['medium']
        ),
        showarrow=False,
        xanchor='center'
    )
    
    # Add trend if provided
    if trend is not None:
        fig.add_annotation(
            x=0.9, y=0.85,
            text=trend_text,
            font=dict(
                family=FONTS['body']['family'],
                size=14,
                color=trend_color
            ),
            showarrow=False,
            xanchor='right',
            bgcolor='rgba(255, 255, 255, 0.8)',
            borderpad=5
        )
    
    # Update layout
    fig.update_layout(
        height=150,
        margin=dict(t=10, b=10, l=10, r=10),
        xaxis=dict(visible=False, range=[0, 1]),
        yaxis=dict(visible=False, range=[0, 1]),
        plot_bgcolor='white',
        paper_bgcolor='white',
        hovermode=False
    )
    
    return fig


def create_kpi_row(kpi_data):
    """
    Create a row of KPI cards
    
    Parameters:
    - kpi_data: List of dictionaries containing KPI information
      [{'value': 100, 'label': 'Total', 'icon': '👥', 'trend': 5.2}, ...]
    """
    cards = []
    
    for kpi in kpi_data:
        card = create_kpi_card(
            value=kpi.get('value', 0),
            label=kpi.get('label', 'KPI'),
            icon=kpi.get('icon', '📊'),
            trend=kpi.get('trend'),
            trend_direction=kpi.get('trend_direction', 'up'),
            color=kpi.get('color', COLORS['primary']),
            format_string=kpi.get('format', '{:,.0f}')
        )
        cards.append(card)
    
    return cards


def create_metric_card(title, metrics):
    """
    Create a metric card with multiple values
    
    Parameters:
    - title: Card title
    - metrics: List of dictionaries [{'label': 'Metric', 'value': 100}, ...]
    """
    
    fig = go.Figure()
    
    # Add invisible trace
    fig.add_trace(go.Scatter(
        x=[0, 1],
        y=[0, 1],
        mode='markers',
        marker=dict(size=0, opacity=0),
        showlegend=False
    ))
    
    # Add title
    fig.add_annotation(
        x=0.5, y=0.95,
        text=title,
        font=dict(
            family=FONTS['subtitle']['family'],
            size=FONTS['subtitle']['size'],
            color=COLORS['dark']
        ),
        showarrow=False,
        xanchor='center'
    )
    
    # Add metrics
    num_metrics = len(metrics)
    y_positions = [0.75 - (i * 0.25) for i in range(num_metrics)]
    
    for i, metric in enumerate(metrics):
        # Label
        fig.add_annotation(
            x=0.3, y=y_positions[i],
            text=metric['label'],
            font=dict(
                family=FONTS['body']['family'],
                size=FONTS['body']['size'],
                color=COLORS['medium']
            ),
            showarrow=False,
            xanchor='right'
        )
        
        # Value
        fig.add_annotation(
            x=0.7, y=y_positions[i],
            text=str(metric['value']),
            font=dict(
                family=FONTS['body']['family'],
                size=FONTS['body']['size'],
                color=COLORS['dark']
            ),
            showarrow=False,
            xanchor='left'
        )
    
    fig.update_layout(
        height=200,
        margin=dict(t=10, b=10, l=10, r=10),
        xaxis=dict(visible=False, range=[0, 1]),
        yaxis=dict(visible=False, range=[0, 1]),
        plot_bgcolor='white',
        paper_bgcolor='white',
        hovermode=False
    )
    
    return fig
