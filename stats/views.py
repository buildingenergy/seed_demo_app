from django.contrib.auth.decorators import login_required
from annoying.decorators import render_to
from seed.models import BuildingSnapshot
from django.db.models import Avg


@login_required
@render_to('stats/stats.html')
def stats(request):
    """average EUI"""
    stats_dict = BuildingSnapshot.objects.filter(
        canonical_building__active=True
    ).aggregate(Avg('gross_floor_area'))
    stats_dict.update(
        BuildingSnapshot.objects.filter(
            canonical_building__active=True
        ).aggregate(Avg('year_built'))
    )
    return locals()
