import os, sys
from rich.table import Table
from rich.live import Live
from rich import box
from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt

userConversionInfo = ["--", 0]

def Convertor():
  
  global userConversionInfo
  
  with Live():
  
      os.system("Cls")
  
      table = Table(show_lines=True, box=box.SQUARE)
  
      table.add_column("From Unit", style="yellow")
      table.add_column("To Unit", style="blue")
      table.add_column("Value", justify="center")
  
      conversions = {
    # Length
    "km-mile":              lambda km: km * 0.621371,
    "mile-km":              lambda miles: miles / 0.621371,
    "meter-yard":           lambda m: m * 1.09361,
    "yard-meter":           lambda yd: yd / 1.09361,
    "inch-cm":              lambda inch: inch * 2.54,
    "cm-inch":              lambda cm: cm / 2.54,
    "foot-meter":           lambda ft: ft * 0.3048,
    "meter-foot":           lambda m: m / 0.3048,
    "mm-inch":              lambda mm: mm / 25.4,
    "inch-mm":              lambda inch: inch * 25.4,

    # Mass
    "kg-pound":             lambda kg: kg * 2.20462,
    "pound-kg":             lambda lb: lb / 2.20462,
    "gram-ounce":           lambda g: g * 0.035274,
    "ounce-gram":           lambda oz: oz / 0.035274,
    "mg-gram":              lambda mg: mg / 1000,
    "gram-mg":              lambda g: g * 1000,
    "tonne-kg":             lambda t: t * 1000,
    "kg-tonne":             lambda kg: kg / 1000,
    "stone-kg":             lambda st: st * 6.35029,
    "kg-stone":             lambda kg: kg / 6.35029,

    # Volume
    "liter-gallon":         lambda l: l * 0.264172,
    "gallon-liter":         lambda gal: gal / 0.264172,
    "ml-liter":             lambda ml: ml / 1000,
    "liter-ml":             lambda l: l * 1000,
    "cup-liter":            lambda cup: cup * 0.24,
    "liter-cup":            lambda l: l / 0.24,
    "pint-liter":           lambda pt: pt * 0.473176,
    "liter-pint":           lambda l: l / 0.473176,
    "quart-liter":          lambda qt: qt * 0.946353,
    "liter-quart":          lambda l: l / 0.946353,

    # Area
    "sqmeter-sqfoot":       lambda m2: m2 * 10.7639,
    "sqfoot-sqmeter":       lambda ft2: ft2 / 10.7639,
    "hectare-acre":         lambda ha: ha * 2.47105,
    "acre-hectare":         lambda ac: ac / 2.47105,
    "sqkm-sqmile":          lambda km2: km2 * 0.386102,
    "sqmile-sqkm":          lambda mi2: mi2 / 0.386102,

    # Temperature
    "celsius-fahrenheit":   lambda c: (c * 9/5) + 32,
    "fahrenheit-celsius":   lambda f: (f - 32) * 5/9,
    "celsius-kelvin":       lambda c: c + 273.15,
    "kelvin-celsius":       lambda k: k - 273.15,

    # Time
    "hour-minute":          lambda hr: hr * 60,
    "minute-hour":          lambda min: min / 60,
    "minute-second":        lambda min: min * 60,
    "second-minute":        lambda sec: sec / 60,
    "day-hour":             lambda d: d * 24,
    "hour-day":             lambda hr: hr / 24,

    # Speed
    "kph-mph":              lambda kph: kph * 0.621371,
    "mph-kph":              lambda mph: mph / 0.621371,

    # Pressure
    "atm-pascal":           lambda atm: atm * 101325,
    "pascal-atm":           lambda pa: pa / 101325,
    "bar-pascal":           lambda bar: bar * 100000,
    "pascal-bar":           lambda pa: pa / 100000,

    # Energy
    "joule-calorie":        lambda j: j / 4.184,
    "calorie-joule":        lambda cal: cal * 4.184,

    # Fallback
    "--":                   lambda v: 0
}

  
      conversionCatch = list(conversions.keys())
  
      for conversion in conversionCatch:
        
        FromUnit = conversion.split("-")[0].capitalize()
        ToUnit = conversion.split("-")[1].capitalize()
        
        if conversion == userConversionInfo[0]:
            con = userConversionInfo[0]
            value = userConversionInfo[1]
            
        else: 
          con = "--"
          value = 0  
        
        if "--" not in conversion: 
          table.add_row(FromUnit, ToUnit, f"{round((conversions[con](value)) * 1000) / 1000}")
    
      Console().print(table)

      conversion = Prompt.ask("[green]Convertion[/][green][/]").lower()
      
      conversion = conversion.split(", ")
      
      conversion = [item.replace(" -> ", "-") for item in conversion]
      
      userConversionInfo = conversion
      
      userConversionInfo[1] = int(userConversionInfo[1])
  
Convertor()  
