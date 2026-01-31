import streamlit as st
from datetime import datetime, timedelta
from typing import List, Dict, Any


st.set_page_config(page_title="AI Operator SOP & Test UI", layout="wide")


# ------------------------------
# Data and helpers
# ------------------------------

def _dt(days_ago: int) -> datetime:
    return datetime.now() - timedelta(days=days_ago)


def _txn(ts_days_ago: int, amount: float, merchant: str) -> Dict[str, Any]:
    return {
        "timestamp": datetime.now() - timedelta(days=ts_days_ago),
        "amount": amount,
        "merchant": merchant,
    }


def load_sample_cases() -> List[Dict[str, Any]]:
    return [
        {
            "case_id": "C-1001",
            "status": "Needs Review",
            "created_at": _dt(5),
            "user_name": "Avery Chen",
            "account_balance": 1240.55,
            "alert_triggers": [
                {"title": "Unusual location", "timestamp": _dt(4)},
                {"title": "High velocity", "timestamp": _dt(3)},
                {"title": "New device", "timestamp": _dt(2)},
            ],
            "transactions": [
                _txn(2, 55.10, "Blue Bottle"),
                _txn(3, 120.00, "Best Buy"),
                _txn(5, 12.49, "Trader Joe's"),
                _txn(12, 9.99, "Spotify"),
                _txn(18, 40.00, "Uber"),
                _txn(29, 210.00, "Airbnb"),
                _txn(31, 5.25, "Starbucks"),
                _txn(33, 18.70, "Whole Foods"),
                _txn(45, 60.00, "Target"),
                _txn(52, 11.15, "Chipotle"),
                _txn(57, 7.80, "Lyft"),
            ],
        },
        {
            "case_id": "C-1002",
            "status": "Needs Review",
            "created_at": _dt(3),
            "user_name": "Jordan Reyes",
            "account_balance": 220.00,
            "alert_triggers": [
                {"title": "Multiple declines", "timestamp": _dt(2)},
            ],
            "transactions": [
                _txn(1, 18.95, "Whole Foods"),
                _txn(7, 140.00, "Apple"),
                _txn(28, 8.99, "Netflix"),
                _txn(35, 6.50, "Starbucks"),
            ],
        },
        {
            "case_id": "C-1003",
            "status": "Needs Review",
            "created_at": _dt(1),
            "user_name": "Priya Singh",
            "account_balance": 980.75,
            "alert_triggers": [
                {"title": "Password reset", "timestamp": _dt(1)},
                {"title": "New payee added", "timestamp": _dt(1)},
            ],
            "transactions": [
                _txn(1, 25.00, "Doordash"),
                _txn(2, 14.30, "Amazon"),
                _txn(40, 120.00, "Southwest"),
            ],
        },
        {
            "case_id": "C-1004",
            "status": "Needs Review",
            "created_at": _dt(2),
            "user_name": "Miguel Alvarez",
            "account_balance": None,
            "alert_triggers": [],
            "transactions": [
                _txn(2, 65.00, "REI"),
                _txn(3, 23.00, "Shell"),
                _txn(29, 41.00, "Costco"),
                _txn(34, 18.25, "Safeway"),
            ],
        },
        {
            "case_id": "C-1005",
            "status": "Needs Review",
            "created_at": _dt(7),
            "user_name": "Lena Park",
            "account_balance": 52.40,
            "alert_triggers": [
                {"title": "Large transfer", "timestamp": _dt(6)},
                {"title": "Account takeover", "timestamp": _dt(6)},
                {"title": "Beneficiary change", "timestamp": _dt(5)},
                {"title": "Unusual merchant", "timestamp": _dt(5)},
            ],
            "transactions": [
                _txn(1, 3.50, "Subway"),
                _txn(2, 9.99, "Hulu"),
                _txn(3, 64.00, "Home Depot"),
                _txn(4, 12.15, "Taco Bell"),
                _txn(5, 16.80, "Target"),
                _txn(6, 7.25, "7-Eleven"),
                _txn(8, 8.20, "Trader Joe's"),
                _txn(9, 110.00, "United"),
                _txn(10, 18.00, "CVS"),
                _txn(11, 22.50, "Amazon"),
                _txn(12, 45.10, "Walmart"),
                _txn(13, 14.75, "Walgreens"),
            ],
        },
        {
            "case_id": "C-1006",
            "status": "Complete",
            "created_at": _dt(9),
            "user_name": "Samira Noor",
            "account_balance": 1500.00,
            "alert_triggers": [
                {"title": "Chargeback", "timestamp": _dt(8)},
            ],
            "transactions": [
                _txn(2, 70.00, "Wayfair"),
                _txn(33, 15.00, "Peet's"),
            ],
        },
        {
            "case_id": "C-1007",
            "status": "Complete",
            "created_at": _dt(15),
            "user_name": "Oliver Brooks",
            "account_balance": 310.00,
            "alert_triggers": [
                {"title": "Login anomaly", "timestamp": _dt(14)},
                {"title": "High spend", "timestamp": _dt(13)},
            ],
            "transactions": [
                _txn(10, 33.00, "Target"),
                _txn(20, 54.20, "REI"),
                _txn(40, 88.00, "Delta"),
            ],
        },
        {
            "case_id": "C-1008",
            "status": "Needs Review",
            "created_at": _dt(10),
            "user_name": "Nina Patel",
            "account_balance": 860.10,
            "alert_triggers": [
                {"title": "Password reset", "timestamp": _dt(9)},
                {"title": "Unusual IP", "timestamp": _dt(8)},
                {"title": "High velocity", "timestamp": _dt(8)},
            ],
            "transactions": [
                _txn(3, 15.99, "Spotify"),
                _txn(4, 75.00, "Best Buy"),
                _txn(6, 18.00, "Uber"),
                _txn(8, 22.10, "Target"),
                _txn(9, 44.00, "Apple"),
                _txn(12, 5.50, "Starbucks"),
                _txn(15, 19.99, "Hulu"),
                _txn(16, 7.45, "Chipotle"),
                _txn(17, 2.99, "Amazon"),
                _txn(18, 65.00, "REI"),
                _txn(19, 12.00, "CVS"),
                _txn(20, 8.75, "Safeway"),
            ],
        },
    ]


def age_in_days(created_at: datetime) -> float:
    delta = datetime.now() - created_at
    return max(delta.total_seconds() / 86400, 0.0)


def txn_count_last_30d(transactions: List[Dict[str, Any]]) -> int:
    cutoff = datetime.now() - timedelta(days=30)
    return sum(1 for t in transactions if t["timestamp"] >= cutoff)


def format_dt(dt: datetime) -> str:
    return dt.strftime("%Y-%m-%d %H:%M")


def generate_summary(case: Dict[str, Any]) -> Dict[str, Any]:
    age_days = age_in_days(case["created_at"])
    txn_count = txn_count_last_30d(case["transactions"])
    balance = case.get("account_balance")
    triggers = case.get("alert_triggers", [])
    num_triggers = len(triggers)
    balance_str = f"${balance:,.2f}" if balance is not None else "Not available"

    if txn_count > 10 and num_triggers > 2:
        disposition = "Escalate"
    else:
        disposition = "Close"

    if triggers:
        trigger_lines = [f"- {t['title']} ({format_dt(t['timestamp'])})" for t in triggers]
    else:
        trigger_lines = ["- Not available"]

    summary_lines = [
        f"Case {case['case_id']} for {case['user_name']} is open for {age_days:.1f} day(s).",
        f"Transactions in last 30 days: {txn_count}.",
        f"Current balance: {balance_str}.",
        "Alert triggers:",
        *trigger_lines,
        f"Disposition: {disposition}.",
    ]

    return {
        "summary": "\n".join(summary_lines),
        "txn_count": txn_count,
        "balance_str": balance_str,
        "num_triggers": num_triggers,
        "disposition": disposition,
    }


def ensure_state() -> None:
    if "cases" not in st.session_state:
        st.session_state.cases = load_sample_cases()
    if "filters_applied" not in st.session_state:
        st.session_state.filters_applied = False
    if "filter_status" not in st.session_state:
        st.session_state.filter_status = "Needs Review"
    if "filter_open_more_than" not in st.session_state:
        st.session_state.filter_open_more_than = "2 days"
    if "current_case_id" not in st.session_state:
        st.session_state.current_case_id = None
    if "screen" not in st.session_state:
        st.session_state.screen = "queue"
    if "case_summaries" not in st.session_state:
        st.session_state.case_summaries = {}
    if "audit_log" not in st.session_state:
        st.session_state.audit_log = []


# ------------------------------
# UI components
# ------------------------------

def render_sop() -> None:
    st.header("AI Operator SOP")
    st.subheader("Purpose")
    st.write(
        "This SOP defines an exact, deterministic workflow for processing cases using the **Operator Test UI**. "
        "Follow each step in order. Use only the specified UI elements and labels."
    )

    st.subheader("Rules for which cases to process")
    st.markdown(
        "1. Navigate to **Operator Test UI** ➜ **Case Queue**.\n"
        "2. Set filter **Status** to `Needs Review`.\n"
        "3. Set filter **Open for more than** to `2 days` (or higher).\n"
        "4. Click **Apply filters**.\n"
        "5. Only rows displayed after filtering are eligible. Do not process any case not shown."
    )

    st.subheader("Step-by-step procedure")
    st.markdown(
        "1. In **Case Queue**, for the first row shown, click its **Review** button.\n"
        "2. The screen changes to **Case Details**. Confirm the case ID at the top.\n"
        "3. Read the data from these sections (do not infer):\n"
        "   - **Transactions (Last 30 Days)** ➜ \"Transactions in last 30 days: X\".\n"
        "   - **Account Summary** ➜ \"Current balance: ...\".\n"
        "   - **Alert Triggers** ➜ each trigger title and timestamp.\n"
        "4. Click **Generate summary**.\n"
        "5. In **Case summary**, verify text is populated.\n"
        "6. Click **Mark complete**.\n"
        "7. Click **Back to queue**.\n"
        "8. Repeat steps 1–7 for each remaining row in **Case Queue**."
    )

    st.subheader("Data extraction checklist")
    st.markdown(
        "- Transactions count last 30 days\n"
        "- Current balance\n"
        "- Alert triggers list with timestamps"
    )

    st.subheader("Completion definition")
    st.markdown(
        "A case is complete when all conditions are true:\n"
        "1. **Case summary** contains text.\n"
        "2. **Mark complete** has been clicked.\n"
        "3. The case no longer appears in **Case Queue** when **Status** = `Needs Review`."
    )

    st.subheader("Edge cases")
    st.markdown(
        "- If any required data is missing, show `Not available` in the UI and still generate a summary.\n"
        "- **Mark complete** must remain disabled until a summary has been generated."
    )


def render_filters() -> None:
    col1, col2, col3 = st.columns([2, 2, 1])
    with col1:
        status = st.selectbox(
            "Status",
            ["Needs Review", "Complete"],
            index=0 if st.session_state.filter_status == "Needs Review" else 1,
        )
    with col2:
        open_more_than = st.selectbox(
            "Open for more than",
            ["1 day", "2 days", "3 days", "7 days"],
            index=["1 day", "2 days", "3 days", "7 days"].index(
                st.session_state.filter_open_more_than
            ),
        )
    with col3:
        st.write("\n")
        if st.button("Apply filters"):
            st.session_state.filter_status = status
            st.session_state.filter_open_more_than = open_more_than
            st.session_state.filters_applied = True


def render_case_queue() -> None:
    st.title("Case Queue")
    render_filters()

    if not st.session_state.filters_applied:
        st.info("Select filters and click Apply filters to view the queue.")
        return

    status_filter = st.session_state.filter_status
    threshold_label = st.session_state.filter_open_more_than
    threshold_days = int(threshold_label.split()[0])

    filtered_cases = []
    for c in st.session_state.cases:
        age = age_in_days(c["created_at"])
        if c["status"] == status_filter and age > threshold_days:
            filtered_cases.append(c)

    if not filtered_cases:
        st.warning("No cases match the current filters.")
        return

    st.subheader("Cases matching filters")

    for case in filtered_cases:
        age = age_in_days(case["created_at"])
        with st.container(border=True):
            c1, c2, c3, c4, c5, c6, c7 = st.columns([1.3, 1.5, 1.6, 1, 2, 2, 1])
            c1.write(case["case_id"])
            c2.write(case["status"])
            c3.write(case["created_at"].strftime("%Y-%m-%d"))
            c4.write(f"{age:.1f}")
            c5.write(case["user_name"])
            reason = (
                case["alert_triggers"][0]["title"]
                if case["alert_triggers"]
                else "No triggers"
            )
            c6.write(reason)
            if c7.button("Review", key=f"review_{case['case_id']}"):
                st.session_state.current_case_id = case["case_id"]
                st.session_state.screen = "details"
                st.rerun()


def render_account_summary(case: Dict[str, Any]) -> None:
    balance = case.get("account_balance")
    balance_str = f"${balance:,.2f}" if balance is not None else "Not available"
    st.markdown("### Account Summary")
    st.write(f"Current balance: {balance_str}")


def render_transactions(case: Dict[str, Any]) -> int:
    st.markdown("### Transactions (Last 30 Days)")
    cutoff = datetime.now() - timedelta(days=30)
    recent = [t for t in case["transactions"] if t["timestamp"] >= cutoff]
    st.write(f"Transactions in last 30 days: {len(recent)}")

    if recent:
        table = [
            {
                "timestamp": format_dt(t["timestamp"]),
                "amount": f"${t['amount']:.2f}",
                "merchant": t["merchant"],
            }
            for t in sorted(recent, key=lambda x: x["timestamp"], reverse=True)
        ]
        st.dataframe(table, use_container_width=True)
    else:
        st.write("No transactions in the last 30 days.")
    return len(recent)


def render_alert_triggers(case: Dict[str, Any]) -> int:
    st.markdown("### Alert Triggers")
    triggers = case.get("alert_triggers", [])
    if triggers:
        for t in triggers:
            st.write(f"- {t['title']} ({format_dt(t['timestamp'])})")
    else:
        st.write("Not available")
    return len(triggers)


def render_case_details() -> None:
    case_id = st.session_state.current_case_id
    case = next((c for c in st.session_state.cases if c["case_id"] == case_id), None)
    if not case:
        st.error("Case not found.")
        st.session_state.screen = "queue"
        return

    st.title("Case Details")
    st.write(f"Case ID: {case['case_id']}")

    render_account_summary(case)
    txn_count = render_transactions(case)
    trigger_count = render_alert_triggers(case)

    summary_payload = st.session_state.case_summaries.get(case_id)

    col1, col2, col3 = st.columns([1.2, 1.2, 1.2])
    with col1:
        if st.button("Generate summary"):
            summary_payload = generate_summary(case)
            st.session_state.case_summaries[case_id] = summary_payload
    with col2:
        summary_text = summary_payload["summary"] if summary_payload else ""
        st.text_area("Case summary", value=summary_text, height=200)
    with col3:
        can_complete = bool(summary_payload)
        if st.button("Mark complete", disabled=not can_complete):
            case["status"] = "Complete"
            completed_at = datetime.now().strftime("%Y-%m-%d %H:%M")
            st.session_state.audit_log.append(
                {
                    "case_id": case_id,
                    "completed_at": completed_at,
                    "transaction_count_30d": summary_payload["txn_count"],
                    "account_balance": summary_payload["balance_str"],
                    "num_triggers": summary_payload["num_triggers"],
                    "disposition": summary_payload["disposition"],
                }
            )
            st.session_state.current_case_id = None
            st.session_state.screen = "queue"
            st.rerun()

    st.button("Back to queue", on_click=_back_to_queue)


def _back_to_queue() -> None:
    st.session_state.current_case_id = None
    st.session_state.screen = "queue"
    st.rerun()


def render_audit_log() -> None:
    with st.expander("Audit Log"):
        if not st.session_state.audit_log:
            st.write("No completed cases yet.")
            return
        st.dataframe(st.session_state.audit_log, use_container_width=True)


def render_operator_ui() -> None:
    if st.session_state.screen == "details" and st.session_state.current_case_id:
        render_case_details()
    else:
        render_case_queue()
    render_audit_log()


def main() -> None:
    ensure_state()
    tab1, tab2 = st.tabs(["SOP", "Operator Test UI"])
    with tab1:
        render_sop()
    with tab2:
        render_operator_ui()


if __name__ == "__main__":
    main()
