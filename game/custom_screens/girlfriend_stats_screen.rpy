define STATS_SIZE = 25

screen girlfriend_stats():
    $ gf_stats_summary = girlfriend.stats_summary()
    vbox:
        xalign 0
        yalign 0
        spacing 8
        frame:
            xpadding 15
            ypadding 10
            xalign 0.5
            yalign 0.5
            text "{size=[STATS_SIZE]}Time: [gametime.display()]\n[gf_stats_summary]"