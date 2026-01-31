class ActionPlannerAgent:
    def generate_action_plan(self, summary: dict, impact: dict, validation: dict) -> dict:
        plan = []

        default_owner = "Compliance"
        if impact.get("departments"):
            default_owner = impact["departments"][0]

        if summary.get("obligations"):
            plan.append({
                "action": "Review obligations and map to internal policies",
                "responsible_department": default_owner,
                "priority": "High"
            })

        if impact.get("departments"):
            plan.append({
                "action": "Notify impacted departments",
                "responsible_department": default_owner,
                "priority": "Medium"
            })

        if validation.get("validation_status") == "needs_review":
            plan.append({
                "action": "Resolve items marked for review",
                "responsible_department": "Legal/Compliance",
                "priority": "High"
            })

        if not plan:
            plan.append({
                "action": "No immediate actions identified",
                "responsible_department": default_owner,
                "priority": "Low"
            })

        return plan
