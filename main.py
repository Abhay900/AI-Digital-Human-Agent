from app.agents.script_analyzer import ScriptAnalyzer


analyzer = ScriptAnalyzer()

result = analyzer.analyze(
    "A presenter explains why planning is important."
)

print(result)