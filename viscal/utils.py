def relative_improvement(loss_curve):
    """Convert loss curve to relative improvement (%)"""
    L_start = loss_curve[0]
    return (L_start - loss_curve) / L_start * 100