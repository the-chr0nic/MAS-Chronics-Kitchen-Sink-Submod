# Register the submod
init -990 python:
    store.mas_submod_utils.Submod(
        author="chronic",
        name="Chronic's Kitchen Sink Submod",
        description="A submod containing a little bit of everything!",
        version="1.0.0"
    )

# Register the updater
init -989 python:
    if store.mas_submod_utils.isSubmodInstalled("Submod Updater Plugin"):
        store.sup_utils.SubmodUpdater(
            submod="Chronic's Kitchen Sink Submod",
            user_name="the-chr0nic",
            repository_name="MAS-Chronics-Kitchen-Sink-Submod"
        )
