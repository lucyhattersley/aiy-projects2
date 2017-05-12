    # =========================================
    # Makers! Add your own voice commands here.
    # =========================================

    actor.add_keyword('light on', GpioWrite(4, True))
    actor.add_keyword('light off', GpioWrite(4, False))