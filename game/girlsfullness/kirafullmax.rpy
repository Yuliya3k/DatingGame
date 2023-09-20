label kirafullmax:
    if g1_fullness >= g1_fullmax*0.5 and g1_fullmax < kira_abolutemaxfullness:
        $ g1_fullmax += 50        
    else:
        if g1_fullness <= 0 and g1_fullmax > 800:
            $ g1_fullmax -= 50
        else:
            pass

return