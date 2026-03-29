# 💖 Interactive Electric Field with Two Charges (Proper Display) 💖

import numpy as np
import matplotlib.pyplot as plt
from ipywidgets import FloatSlider, interactive
from IPython.display import display

# --- Grid ---
Nx, Ny = 200, 200
x = np.linspace(-1, 1, Nx)
y = np.linspace(-1, 1, Ny)
X, Y = np.meshgrid(x, y)

def update_plot(q1_x=-0.3, q1_y=0.0, q1_val=1.0,
                q2_x=0.3, q2_y=0.0, q2_val=-1.0):
    
    plt.clf()
    fig, ax = plt.subplots(figsize=(6,6))
    
    # --- Distances to charges ---
    R1 = np.sqrt((X - q1_x)**2 + (Y - q1_y)**2) + 1e-3  # avoid div by 0
    R2 = np.sqrt((X - q2_x)**2 + (Y - q2_y)**2) + 1e-3
    
    # --- Electric field magnitude ---
    E1 = q1_val / R1**2
    E2 = q2_val / R2**2
    E = E1 + E2
    
    # --- Normalize field for display ---
    E_plot = np.tanh(E * 0.5)  # compress extremes for visualization
    
    # --- Plot field ---
    im = ax.imshow(E_plot, extent=[-1,1,-1,1], origin='lower', cmap='rainbow')
    
    # --- Draw charges ---
    ax.scatter(q1_x, q1_y, color='red', s=200, label="Positive", zorder=10)
    ax.scatter(q2_x, q2_y, color='blue', s=200, label="Negative", zorder=10)
    
    # --- Labels & style ---
    ax.set_title("Electric Field of Two Charges", fontsize=14, color='deeppink')
    ax.set_xlabel("x", color='deeppink')
    ax.set_ylabel("y", color='deeppink')
    ax.set_facecolor('mistyrose')
    ax.legend()
    
    # --- Colorbar ---
    if not hasattr(update_plot, "colorbar"):
        update_plot.colorbar = plt.colorbar(im, ax=ax, label="Normalized Field (a.u.)")
    else:
        update_plot.colorbar.update_normal(im)
    
    plt.show()

# --- Sliders ---
slider_q1_x = FloatSlider(min=-0.9, max=0.0, step=0.01, value=-0.3, description="Charge1 X:", style={'description_width':'initial'})
slider_q1_y = FloatSlider(min=-0.9, max=0.9, step=0.01, value=0.0, description="Charge1 Y:", style={'description_width':'initial'})
slider_q1_val = FloatSlider(min=0.1, max=5.0, step=0.1, value=1.0, description="Charge1 (+):", style={'description_width':'initial'})

slider_q2_x = FloatSlider(min=0.0, max=0.9, step=0.01, value=0.3, description="Charge2 X:", style={'description_width':'initial'})
slider_q2_y = FloatSlider(min=-0.9, max=0.9, step=0.01, value=0.0, description="Charge2 Y:", style={'description_width':'initial'})
slider_q2_val = FloatSlider(min=-5.0, max=-0.1, step=0.1, value=-1.0, description="Charge2 (-):", style={'description_width':'initial'})

interactive_plot = interactive(
    update_plot,
    q1_x=slider_q1_x, q1_y=slider_q1_y, q1_val=slider_q1_val,
    q2_x=slider_q2_x, q2_y=slider_q2_y, q2_val=slider_q2_val
)
display(interactive_plot)