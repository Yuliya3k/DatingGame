label choosebike:

    $ position = "linbikeparklisteningclose"
    call sceneimg

    menu:
        

        ######################################################################
        # ── HOW TO CHOOSE a bike ────────────────────────────────────────────
        "How to choose":

            if not _seen_choose:
                $ _seen_choose = True

                # Lin talks
                $ position = "linbikeparktalkclose"
                call sceneimg
                Lin "Rule one: the bike fits you—*not* the other way around. If the frame feels like a rented tux, keep shopping."

                # Player
                $ position = "linbikeparklisteningclose"
                call sceneimg
                player "So I shouldn’t buy the pretty carbon rocket just because it’s on sale?"

                # Lin
                $ position = "linbikeparktalkclose"
                call sceneimg
                Lin "Only if you can reach the bars without turning into Quasimodo. Size, then saddle, then components. Paint last."

            else:
                $ position = "linbikeparktalkclose"
                call sceneimg
                Lin "Fit first, flashy bits later—remember?"

        ######################################################################
        # ── Health benefits ─────────────────────────────────────────────────
        "What are health benefits":

            if not _seen_health:
                $ _seen_health = True

                $ position = "linbikeparktalkclose"
                call sceneimg
                Lin "Cardio without knee‑pounding impact, core engagement on every climb, and legs that can carry groceries for days."

                $ position = "linbikeparklisteningclose"
                call sceneimg
                player "Plus the smug glow of saving the planet one commute at a time."

                $ position = "linbikeparktalkclose"
                call sceneimg
                Lin "Exactly. Endorphins, vitamin D, and zero parking tickets."

            else:
                $ position = "linbikeparktalkclose"
                call sceneimg
                Lin "Same perks: strong heart, happy brain, bulletproof quads."

        ######################################################################
        # ── Riding history ─────────────────────────────────────────────────
        "How long does she ride":

            if not _seen_history:
                $ _seen_history = True

                $ position = "linbikeparktalkclose"
                call sceneimg
                Lin "First ride? Age fourteen. Rusty ten‑speed, brakes like wet soap. Still felt like wings."

                $ position = "linbikeparklisteningclose"
                call sceneimg
                player "And now you’re flying on carbon and coaching mortals like me."

                $ position = "linbikeparktalkclose"
                call sceneimg
                Lin "Upgraded gear, same freedom buzz."

            else:
                $ position = "linbikeparktalkclose"
                call sceneimg
                Lin "Fourteen, rust bucket, never looked back—you know the drill."

    return
