from pathlib import Path

script_path = Path(".agents/skills/quality_compliance_auditor/scripts/audit_package.py")
code = script_path.read_text(encoding="utf-8")

# Insert duplicate link check and html sync check right after category check
target = """            # Category 28 Science & Tech
            cat_id = meta.get("long_form", {}).get("upload_settings", {}).get("category_id")
            add_check("Metadata", "YouTube Category 28", cat_id == "28", f"Category ID: {cat_id} (Science & Technology)")"""

replacement = """            # Category 28 Science & Tech
            cat_id = meta.get("long_form", {}).get("upload_settings", {}).get("category_id")
            add_check("Metadata", "YouTube Category 28", cat_id == "28", f"Category ID: {cat_id} (Science & Technology)")

            # Check 19: No Duplicate Link Blocks in Description
            desc = meta.get("long_form", {}).get("description", "")
            lines = [l.strip() for l in desc.splitlines() if l.strip().startswith("👉 http") or l.strip().startswith("⭐ http")]
            has_dup_links = len(lines) != len(set(lines))
            add_check("Metadata", "No Duplicate Link Stacks", not has_dup_links, "Zero duplicated links/callout stacks in description")

            # Check 20: HTML Dashboard Sync Check
            html_file = os.path.join(os.path.dirname(base_dir), "index.html")
            if os.path.exists(html_file):
                with open(html_file, "r", encoding="utf-8") as hf:
                    html_content = hf.read()
                # Check if dashboard contains repeated affiliate URL in textarea
                ta_idx = html_content.find('id="videoDescription"')
                if ta_idx != -1:
                    ta_end = html_content.find('</textarea>', ta_idx)
                    ta_text = html_content[ta_idx:ta_end]
                    ta_aff_count = ta_text.count(expected_affiliate) if expected_affiliate else 0
                    # Expect max 2 occurrences (top CTA and enterprise tools)
                    clean_ta = ta_aff_count <= 2
                    add_check("Dashboard", "Description HTML No Slop", clean_ta, f"Affiliate link appears {ta_aff_count} times in textarea (<= 2 allowed)")
                else:
                    add_check("Dashboard", "Description HTML No Slop", True, "Textarea not present or external")"""

if target in code:
    code = code.replace(target, replacement)
    script_path.write_text(code, encoding="utf-8")
    print("Successfully enhanced audit_package.py with duplicate link and dashboard HTML audit checks!")
else:
    print("Target not found in audit_package.py")
