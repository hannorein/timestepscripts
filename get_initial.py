import rebound
rebound.horizons.SSL_CONTEXT = "unverified"
sim = rebound.Simulation()
sim.add(["Sun", "Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"])
sim.save_to_file("initial.bin")
