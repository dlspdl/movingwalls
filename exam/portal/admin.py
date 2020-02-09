from django.contrib import admin

from portal.models import Airport
from portal.models import Fare
from portal.models import FareFormula
from portal.models import Hotel
from portal.models import Location
from portal.models import TravelDetails
from portal.models import Vehicle

@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
  search_fields = ['name', 'longitude', 'latitude', 'tier']
  list_display = ('name', 'longitude', 'latitude', 'tier')
  list_filter = ('name',)

@admin.register(Vehicle)
class VehicleAdmin(admin.ModelAdmin):
  search_fields = ['name']
  list_display = ('name',)
  list_filter = ('name',)

@admin.register(Airport)
class AirportAdmin(admin.ModelAdmin):
  search_fields = ['name','location','capacity']
  list_display = ('name','location','capacity')
  list_filter = ('name',)

admin.site.register(Fare)
admin.site.register(FareFormula)
admin.site.register(Hotel)
admin.site.register(TravelDetails)
