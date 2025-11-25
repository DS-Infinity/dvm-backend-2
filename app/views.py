from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Ticket, Station
from django.contrib.auth.models import User
from .utils import shortest_route

def landing(request):
    return render(request, "app/landing.html")

@login_required
def dashboard(request):
    # get all tickets from the database whose user is request.user
    tickets = Ticket.objects.filter(user=request.user)

    data = {
        'username': request.user.username,
        'tickets': tickets
    }
    
    return render(request, "app/dashboard.html", data)

@login_required
def scan(request):
    return render(request, "app/scan.html")

@login_required
def tickets(request):
    tickets = Ticket.objects.filter(user=request.user)
    stations = Station.objects.all()

    if request.method == "POST":
        start_id = request.POST["start_station"]
        end_id = request.POST["end_station"]

        start = Station.objects.get(id=start_id)
        end = Station.objects.get(id=end_id)

        route = shortest_route(start, end)
        cost = len(route) - 1  # your cost logic

        Ticket.objects.create(
            user=request.user,
            start=start,
            end=end,
            status="Active",
        )

        return render(
            request,
            "app/tickets.html",
            {
                "tickets": tickets,
                "stations": stations,
                "cost": cost,
                "route": route,
            },
        )

    return render(request, "app/tickets.html", {"tickets": tickets, "stations": stations})


from django.http import JsonResponse

@login_required
def path_data(request):
    start_id = request.GET.get("start")
    end_id = request.GET.get("end")

    if not start_id or not end_id:
        return JsonResponse({"cost": None})

    start = Station.objects.get(id=start_id)
    end = Station.objects.get(id=end_id)

    route = shortest_route(start, end)
    cost = len(route) - 1 if route else None

    return JsonResponse({"cost": cost, "path": [f"{station.name} ({station.line})" for station in route] if route else None})



# for admins
# @login_required
# def admin_panel(request):
#     if not request.user.is_staff:
#         return render(request, "app/403.html")  # or redirect to a 'not authorized' page

#     users = User.objects.all()
#     tickets = Ticket.objects.all()
#     stations = Station.objects.all()

#     data = {
#         'users': users,
#         'tickets': tickets,
#         'stations': stations
#     }
    
#     return render(request, "app/admin_panel.html", data)

