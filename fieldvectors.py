# 💖 Interactive Electric Field with Two Charges (Vectors) 💖

import numpy as np
import matplotlib.pyplot as plt
from ipywidgets import FloatSlider, interactive
from IPython.display import display

# --- Grid ---
Nx, Ny = 25, 25  # smaller for arrows so it’s not too crowded
x = np.linspace(-1, 1, Nx)
y = np.linspace(-1, 1, Ny)
X, Y = np.meshgrid(x, y)

def update_plot(q1_x=-0.3, q1_y=0.0, q1_val=1.0,
                q2_x=0.3, q2_y=0.0, q2_val=-1.0):
    
    plt.clf()
    fig, ax = plt.subplots(figsize=(6,6))
    
    # --- Vector distances ---
    dx1 = X - q1_x
    dy1 = Y - q1_y
    R1 = np.sqrt(dx1**2 + dy1**2) + 1e-3
    
    dx2 = X - q2_x
    dy2 = Y - q2_y
    R2 = np.sqrt(dx2**2 + dy2**2) + 1e-3
    
    # --- Electric field vectors ---
    Ex = q1_val*dx1/R1**3 + q2_val*dx2/R2**3
    Ey = q1_val*dy1/R1**3 + q2_val*dy2/R2**3
    
    # --- Normalize for arrows ---
    E_mag = np.sqrt(Ex**2 + Ey**2)
    Ex_norm = Ex / (E_mag + 1e-6)
    Ey_norm = Ey / (E_mag + 1e-6)
    
    # --- Color based on magnitude ---
    colors = plt.cm.rainbow((E_mag / E_mag.max()))
    
    # --- Quiver plot ---
    ax.quiver(X, Y, Ex_norm, Ey_norm, E_mag, pivot='mid', cmap='rainbow', scale=20)
    
    # --- Draw charges ---
    ax.scatter(q1_x, q1_y, color='red', s=200, label="Positive", zorder=10)
    ax.scatter(q2_x, q2_y, color='blue', s=200, label="Negative", zorder=10)
    
    # --- Labels & style ---
    ax.set_title("Electric Field Vectors", fontsize=14, color='deeppink')
    ax.set_xlabel("x", color='deeppink')
    ax.set_ylabel("y", color='deeppink')
    ax.set_facecolor('mistyrose')
    ax.set_xlim([-1,1])
    ax.set_ylim([-1,1])
    ax.legend()
    
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