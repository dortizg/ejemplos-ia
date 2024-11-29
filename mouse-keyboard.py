import pydbus

# Conectar a la sesión de D-Bus del usuario
bus = pydbus.SessionBus()

# Obtener la interfaz de Mutter
mutter = bus.get("org.gnome.Mutter", "/org/gnome/Mutter")

# Mover el cursor del mouse
mutter.MoveCursor(100, 100)

# Simular un clic de mouse
mutter.ClickButton(1)  # Botón izquierdo

# Simular una pulsación de tecla
mutter.KeyPress("Enter")

