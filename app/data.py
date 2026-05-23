from app.schemas import Hospital, HospitalReadinessPoint, Incident, RiskPoint, SummaryMetric, TrendPoint


SUMMARY_METRICS = [
    SummaryMetric(title="Emergency Response Time", value="4m 12s", detail="Down 18% this week"),
    SummaryMetric(title="Lives Assisted Today", value="28,441", detail="Across 6 continents"),
    SummaryMetric(title="Hospitals Online", value="12,480", detail="99.97% uptime"),
    SummaryMetric(title="AI Risk Score", value="0.18", detail="Global average stabilized"),
    SummaryMetric(title="Active Rescue Missions", value="1,284", detail="482 airborne units"),
]

RESPONSE_TREND = [
    TrendPoint(name="Mon", incoming=1280, resolved=1160),
    TrendPoint(name="Tue", incoming=1390, resolved=1214),
    TrendPoint(name="Wed", incoming=1525, resolved=1338),
    TrendPoint(name="Thu", incoming=1492, resolved=1401),
    TrendPoint(name="Fri", incoming=1668, resolved=1522),
    TrendPoint(name="Sat", incoming=1712, resolved=1608),
    TrendPoint(name="Sun", incoming=1580, resolved=1496),
]

RISK_DISTRIBUTION = [
    RiskPoint(name="Flood", value=31),
    RiskPoint(name="Heat", value=17),
    RiskPoint(name="Wildfire", value=19),
    RiskPoint(name="Hospital Surge", value=21),
    RiskPoint(name="Public Safety", value=12),
]

HOSPITAL_READINESS = [
    HospitalReadinessPoint(region="Africa", readiness=82, rural=74),
    HospitalReadinessPoint(region="Europe", readiness=91, rural=84),
    HospitalReadinessPoint(region="Asia", readiness=85, rural=72),
    HospitalReadinessPoint(region="North America", readiness=94, rural=88),
    HospitalReadinessPoint(region="South America", readiness=80, rural=70),
]

INCIDENTS = [
    Incident(
        name="Lagos Flood Response",
        region="Nigeria",
        coordinates=(6.5244, 3.3792),
        severity="critical",
        category="climate",
        status="Rescue teams active",
        summary="Urban flood-stage escalation affecting 18 districts and coastal transport arteries.",
    ),
    Incident(
        name="Lima Heat Support",
        region="Peru",
        coordinates=(-12.0464, -77.0428),
        severity="high",
        category="medical",
        status="Mobile clinics rerouted",
        summary="Heat stress spike near dense informal settlements with pediatric priority routing.",
    ),
    Incident(
        name="Athens Wildfire Corridor",
        region="Greece",
        coordinates=(37.9838, 23.7275),
        severity="high",
        category="climate",
        status="Evacuation route recalculated",
        summary="Wildfire plume spread affecting peri-urban transport and shelter planning.",
    ),
    Incident(
        name="Dhaka Hospital Surge",
        region="Bangladesh",
        coordinates=(23.8103, 90.4125),
        severity="critical",
        category="medical",
        status="Bed capacity constrained",
        summary="Monsoon-linked respiratory admissions and oxygen demand rising across partner hospitals.",
    ),
]

HOSPITALS = [
    Hospital(
        name="Kisumu Regional Trauma Center",
        region="Kenya",
        level="Level 1",
        availability="82% capacity",
        specialties=["trauma", "maternal health", "critical care"],
    ),
    Hospital(
        name="Athens Civil Protection Medical Hub",
        region="Greece",
        level="Level 2",
        availability="76% capacity",
        specialties=["burn care", "respiratory", "evacuation triage"],
    ),
    Hospital(
        name="Dhaka River Basin Emergency Hospital",
        region="Bangladesh",
        level="Level 1",
        availability="94% capacity",
        specialties=["infectious disease", "oxygen therapy", "pediatrics"],
    ),
]

AI_RECOMMENDATIONS = [
    "Prioritize pediatric oxygen delivery in Maputo within 17 minutes.",
    "Activate multilingual shelter guidance for Turkish, Arabic, French, and Swahili channels.",
    "Pre-position blood units O- and B+ across three regional trauma centers.",
    "Enable offline mesh messaging where network quality drops below 2G thresholds.",
]