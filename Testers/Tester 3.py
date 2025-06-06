
from Utility import password
from rich.console import Console

paragraph = '''
Sunshine42 is ready for adventure,
while Ocean7breeze keeps things cool.
Mountain123 stands tall with strength,
and RiverFlow89 moves smoothly through challenges.
ForestTrail56 leads to hidden paths,
and SkyBlue21 opens endless possibilities.
GoldenGate77 guards the treasure,
and SilverMoon9 lights up the night.
DesertStorm44 roars with power,
and AutumnLeaves33 bring calm change.
CrystalLake11 reflects clarity,
and ThunderBolt88 strikes fast.
MorningStar5 shines bright,
while TwilightZone66 brings mystery.
CoralReef99 hides vibrant life,
and Snowflake3 drifts softly.
Wildflower12 blooms freely,
and Horizon360 expands your view.
VelvetSky4 feels soft,
while IronHorse17 charges ahead.
RainbowPath28 brings color to the journey,
and StarDust50 sparkles in the dark.
OceanWave34 crashes with force,
and PineTree72 stands firm.
BlueLagoon58 flows peacefully,
while DesertRose22 thrives in harsh lands.
CloudNine19 lifts spirits high,
and FireFly81 glows gently in the dark.
WinterFrost20 chills the air,
while SummerBreeze30 warms the soul.
MoonLight67 casts a gentle glow,
and RiverStone90 stands steady.
GardenGate24 opens to wonders,
and EmeraldCity15 dazzles with green.
AutumnWind29 whispers secrets,
while LightningFlash42 strikes suddenly.
CoralBay16 is calm and inviting,
and MountainPeak78 reaches the sky.
SilverStream53 flows with grace,
while GoldenField84 shines in the sun.
NightOwl11 stays alert,
and DayDream99 drifts in thought.
OceanMist43 refreshes the mind,
while ForestShade27 cools the day.
FireStorm59 blazes intensely,
and SnowDrift35 moves silently.
CrystalCove13 hides treasures,
while ThunderClap76 shakes the ground.
MeadowBloom18 grows abundantly,
and StarLight64 twinkles far away.
RiverBend48 curves gently,
and DesertDawn33 rises anew.
SkyHigh91 reaches beyond limits,
while ValleyDeep22 holds secrets.
OceanSpray40 refreshes senses,
and PineCone75 is earthy and strong.
CloudBurst61 rains suddenly,
while FireTrail50 burns a path.
WinterMoon25 glows softly,
and SummerSun87 shines brightly.
NightSky39 is vast and mysterious,
while DayLight17 brightens lives.
MountainTrail32 winds upward,
and ForestPath49 leads forward.
GoldenSunset55 warms hearts,
while SilverMoonlight26 calms minds.
CoralReef72 thrives beneath waves,
and RiverStone85 stands firm.
AutumnLeaves44 flutter down,
while ThunderBolt31 strikes fast.
OceanBreeze62 cools gently,
and StarDust78 sparkles far.
PineForest90 is dense and quiet,
while DesertStorm23 roars loudly.
CrystalLake11 reflects peace,
and FireFly34 glows warmly.
WinterFrost45 chills deep,
while SummerBreeze56 warms soft.
SkyBlue27 opens wide,
and RainbowPath69 colors journeys.
NightOwl88 watches keenly,
and DayDream15 drifts freely.
MountainPeak82 rises proudly,
and ForestTrail93 winds smoothly.
GoldenGate64 guards well,
while SilverStream79 flows gently.
CoralBay35 invites rest,
and RiverBend58 curves slowly.
AutumnWind41 whispers secrets,
and LightningFlash20 strikes sharp.
OceanWave57 crashes loudly,
while PineTree36 stands firm.
BlueLagoon50 flows calmly,
and DesertRose13 thrives strong.
CloudNine47 lifts spirits,
and FireStorm84 blazes bright.
WinterMoon22 glows softly,
and SummerSun70 shines warmly.
NightSky53 is deep,
and DayLight31 shines clearly.
MountainTrail60 climbs high,
and ForestPath19 leads on.
GoldenSunset72 warms hearts,
and SilverMoonlight25 soothes minds.
CoralReef77 thrives under waves,
and RiverStone90 stands firm.
AutumnLeaves39 flutter gently,
and ThunderBolt54 strikes fast.
OceanBreeze83 cools softly,
and StarDust68 sparkles brightly.
PineForest91 is quiet,
and DesertStorm24 roars fiercely.
CrystalLake14 reflects calm,
and FireFly37 glows gently.
WinterFrost46 chills softly,
and SummerBreeze57 warms tenderly.
SkyBlue28 opens wide,
and RainbowPath70 colors bright.
NightOwl89 watches closely,
and DayDream16 floats freely.
MountainPeak83 rises high,
and ForestTrail94 winds gently.
GoldenGate65 guards firmly,
and SilverStream80 flows smoothly.
CoralBay36 invites rest,
and RiverBend59 curves slowly.
AutumnWind42 whispers softly,
and LightningFlash21 strikes brightly.
OceanWave58 crashes powerfully,
and PineTree37 stands tall.
BlueLagoon51 flows peacefully,
and DesertRose14 thrives well.
CloudNine48 lifts spirits high,
and FireStorm85 blazes fiercely.
WinterMoon23 glows softly,
and SummerSun71 shines warmly.
NightSky54 is vast,
and DayLight32 shines brightly.
MountainTrail61 climbs steadily,
and ForestPath20 leads onward.
GoldenSunset73 warms hearts deeply,
and SilverMoonlight26 calms minds softly.
CoralReef78 thrives beneath waves,
and RiverStone91 stands firm.
AutumnLeaves40 flutter down slowly,
and ThunderBolt55 strikes fast.
OceanBreeze84 cools gently,
and StarDust69 sparkles far away.
PineForest92 is dense,
and DesertStorm25 roars loudly.
CrystalLake15 reflects peace,
and FireFly38 glows warmly.
WinterFrost47 chills deeply,
and SummerBreeze58 warms softly.
SkyBlue29 opens wide,
and RainbowPath71 colors the journey.
NightOwl90 watches keenly,
and DayDream17 drifts freely.
MountainPeak84 rises proudly,
and ForestTrail95 winds smoothly.
GoldenGate66 guards well,
and SilverStream81 flows gently.
CoralBay37 invites rest,
and RiverBend60 curves slowly.
AutumnWind43 whispers softly,
and LightningFlash22 strikes sharp.
OceanWave59 crashes loudly,
and PineTree38 stands firm.
BlueLagoon52 flows calmly,
and DesertRose15 thrives strongly.
CloudNine49 lifts spirits,
and FireStorm86 blazes bright.
WinterMoon24 glows softly,
and SummerSun72 shines warmly.
NightSky55 is deep,
and DayLight33 shines clearly.
MountainTrail62 climbs high,
and ForestPath21 leads on.
GoldenSunset74 warms hearts,
and SilverMoonlight27 soothes minds.
CoralReef79 thrives under waves,
and RiverStone92 stands steady.
AutumnLeaves41 flutter gently,
and ThunderBolt56 strikes fast.
OceanBreeze85 cools softly,
and StarDust70 sparkles brightly.
PineForest93 is quiet,
and DesertStorm26 roars fiercely.
CrystalLake16 reflects calm,
and FireFly39 glows gently.
WinterFrost48 chills softly,
and SummerBreeze59 warms tenderly.
SkyBlue30 opens wide,
and RainbowPath72 colors bright.
NightOwl91 watches closely,
and DayDream18 floats freely.
MountainPeak85 rises high,
and ForestTrail96 winds gently.
GoldenGate67 guards firmly,
and SilverStream82 flows smoothly.
CoralBay38 invites rest,
and RiverBend61 curves slowly.
AutumnWind44 whispers softly,
and LightningFlash23 strikes brightly.
OceanWave60 crashes powerfully,
and PineTree39 stands tall.
BlueLagoon53 flows peacefully,
and DesertRose16 thrives well.
CloudNine50 lifts spirits high,
and FireStorm87 blazes fiercely.
WinterMoon25 glows softly,
and SummerSun73 shines warmly.
NightSky56 is vast,
and DayLight34 shines brightly.
MountainTrail63 climbs steadily,
and ForestPath22 leads onward.
GoldenSunset75 warms hearts deeply,
and SilverMoonlight28 calms minds softly.
CoralReef80 thrives beneath waves,
and RiverStone93 stands firm.
AutumnLeaves42 flutter down slowly,
and ThunderBolt57 strikes fast.
OceanBreeze86 cools gently,
and StarDust71 sparkles far away.
PineForest94 is dense,
and DesertStorm27 roars loudly.
CrystalLake17 reflects peace,
and FireFly40 glows warmly.
WinterFrost49 chills deeply,
and SummerBreeze60 warms softly.
SkyBlue31 opens wide,
and RainbowPath73 colors the journey.
NightOwl92 watches keenly,
and DayDream19 drifts freely.
MountainPeak86 rises proudly,
and ForestTrail97 winds smoothly.
GoldenGate68 guards well,
and SilverStream83 flows gently.
CoralBay39 invites rest,
and RiverBend62 curves slowly.
AutumnWind45 whispers softly,
and LightningFlash24 strikes sharp.
OceanWave61 crashes loudly,
and PineTree40 stands firm.
BlueLagoon54 flows calmly,
and DesertRose17 thrives strongly.
CloudNine51 lifts spirits,
and FireStorm88 blazes bright.
WinterMoon26 glows softly,
and SummerSun74 shines warmly.
NightSky57 is deep,
and DayLight35 shines clearly.
MountainTrail64 climbs high,
and ForestPath23 leads on.
GoldenSunset76 warms hearts,
and SilverMoonlight29 soothes minds.
CoralReef81 thrives under waves,
and RiverStone94 stands steady.
AutumnLeaves43 flutter gently,
and &#*&%(uHHHH1244 strikes fast.
OceanBreeze87 cools softly,
and StarDust72 sparkles brightly.'''

pwd = password(text = paragraph.replace(".", "").replace(",",""))

print(pwd.identifier())

