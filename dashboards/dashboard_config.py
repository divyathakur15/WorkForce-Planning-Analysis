"""
Professional Dashboard Configuration for Workforce Planning Analysis
Color schemes, themes, and styling constants
"""

# Professional Color Palette - Enhanced with vibrant modern colors
COLORS = {
    # Primary Colors - More vibrant
    'primary': '#2563EB',      # Bright Blue
    'secondary': '#8B5CF6',    # Vivid Purple
    'accent': '#F59E0B',       # Amber Gold
    'tertiary': '#06B6D4',     # Cyan
    
    # Status Colors - More vibrant
    'success': '#10B981',      # Emerald Green
    'warning': '#F59E0B',      # Amber
    'danger': '#EF4444',       # Red
    'info': '#3B82F6',         # Blue
    
    # Neutral Colors
    'dark': '#1F2937',         # Dark Gray
    'medium': '#6B7280',       # Medium Gray
    'light': '#F3F4F6',        # Light Gray
    'white': '#FFFFFF',        # White
    'background': '#F8FAFC',   # Subtle Gray Background
    
    # Gradient Colors - More vibrant
    'gradient_start': '#3B82F6',
    'gradient_mid': '#8B5CF6',
    'gradient_end': '#EC4899',
    
    # Chart Colors (Vibrant Professional Palette)
    'chart_colors': [
        '#2563EB',  # Bright Blue
        '#8B5CF6',  # Vivid Purple
        '#10B981',  # Emerald Green
        '#F59E0B',  # Amber
        '#EF4444',  # Red
        '#06B6D4',  # Cyan
        '#EC4899',  # Pink
        '#14B8A6',  # Teal
        '#F97316',  # Orange
        '#6366F1',  # Indigo
    ],
    
    # Department Colors - More vibrant
    'department_colors': {
        'Human Resources': '#2563EB',
        'Engineering': '#8B5CF6',
        'Sales': '#F59E0B',
        'Marketing': '#10B981',
        'Finance': '#EF4444',
        'Operations': '#06B6D4',
        'IT': '#6366F1',
        'Customer Service': '#EC4899',
        'Research & Development': '#14B8A6',
        'Legal': '#F97316',
    }
}

# Typography
FONTS = {
    'title': {
        'family': 'Segoe UI, Arial, sans-serif',
        'size': 24,
        'weight': 'bold',
        'color': COLORS['dark']
    },
    'subtitle': {
        'family': 'Segoe UI, Arial, sans-serif',
        'size': 18,
        'weight': 600,
        'color': COLORS['dark']
    },
    'body': {
        'family': 'Segoe UI, Arial, sans-serif',
        'size': 14,
        'weight': 'normal',
        'color': COLORS['medium']
    },
    'kpi_value': {
        'family': 'Segoe UI, Arial, sans-serif',
        'size': 36,
        'weight': 'bold',
        'color': COLORS['primary']
    },
    'kpi_label': {
        'family': 'Segoe UI, Arial, sans-serif',
        'size': 12,
        'weight': 600,
        'color': COLORS['medium']
    }
}

# Layout Settings - More compact
LAYOUT = {
    'margin': {'t': 50, 'b': 30, 'l': 30, 'r': 30},
    'padding': 15,
    'card_height': 380,
    'kpi_card_height': 140,
    'border_radius': 12,
    'shadow': '0 4px 12px rgba(0, 0, 0, 0.1)'
}

# Chart Configuration
CHART_CONFIG = {
    'plot_bgcolor': COLORS['white'],
    'paper_bgcolor': COLORS['white'],
    'font': {
        'family': FONTS['body']['family'],
        'size': FONTS['body']['size'],
        'color': FONTS['body']['color']
    },
    'title_font': {
        'family': FONTS['subtitle']['family'],
        'size': FONTS['subtitle']['size'],
        'color': FONTS['subtitle']['color']
    },
    'xaxis': {
        'showgrid': True,
        'gridcolor': COLORS['light'],
        'gridwidth': 1,
        'zeroline': False,
        'showline': True,
        'linewidth': 1,
        'linecolor': COLORS['light']
    },
    'yaxis': {
        'showgrid': True,
        'gridcolor': COLORS['light'],
        'gridwidth': 1,
        'zeroline': False,
        'showline': True,
        'linewidth': 1,
        'linecolor': COLORS['light']
    },
    'hoverlabel': {
        'bgcolor': COLORS['dark'],
        'font_size': 12,
        'font_family': FONTS['body']['family']
    }
}

# KPI Card Templates
KPI_TEMPLATES = {
    'attrition_rate': {
        'icon': '👥',
        'label': 'Attrition Rate',
        'format': '{:.1f}%',
        'color': COLORS['danger'],
        'trend': True
    },
    'retention_rate': {
        'icon': '✓',
        'label': 'Retention Rate',
        'format': '{:.1f}%',
        'color': COLORS['success'],
        'trend': True
    },
    'total_employees': {
        'icon': '👤',
        'label': 'Total Employees',
        'format': '{:,}',
        'color': COLORS['primary'],
        'trend': False
    },
    'avg_tenure': {
        'icon': '📅',
        'label': 'Avg Tenure',
        'format': '{:.1f} years',
        'color': COLORS['info'],
        'trend': True
    },
    'avg_satisfaction': {
        'icon': '😊',
        'label': 'Avg Satisfaction',
        'format': '{:.1f}/5',
        'color': COLORS['success'],
        'trend': True
    },
    'high_risk_employees': {
        'icon': '⚠️',
        'label': 'High Risk',
        'format': '{:,}',
        'color': COLORS['warning'],
        'trend': True
    }
}

# Dashboard Themes
THEMES = {
    'light': {
        'background': '#FFFFFF',
        'card_background': '#FFFFFF',
        'text': COLORS['dark'],
        'border': COLORS['light']
    },
    'dark': {
        'background': '#1F2937',
        'card_background': '#374151',
        'text': '#F9FAFB',
        'border': '#4B5563'
    },
    'corporate': {
        'background': '#F8FAFC',
        'card_background': '#FFFFFF',
        'text': COLORS['dark'],
        'border': '#E2E8F0'
    }
}
