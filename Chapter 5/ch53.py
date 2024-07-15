def take_magic_damage(health, resist, amp, spell_power):
    surge = spell_power * amp
    true_damage = surge - resist
    new_health = health - true_damage
    return new_health



