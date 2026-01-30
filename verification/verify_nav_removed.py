from playwright.sync_api import sync_playwright, expect

def verify_nav_removed():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        try:
            page.goto("http://localhost:8000")

            # Verify Nav
            nav = page.locator("#nav")
            expect(nav).to_be_visible()

            # Check for "Servicios" link - Should NOT exist or be invisible
            # We check the text of all li items
            nav_items = page.locator("#nav ul li").all_inner_texts()
            print(f"Nav items: {nav_items}")

            if "Servicios" not in nav_items and "Artistas" not in nav_items:
                print("Extra links successfully removed.")
            else:
                print("FAILED: Extra links still present.")

            # Take screenshot
            screenshot_path = "/home/jules/verification/verification_nav_removed.png"
            page.screenshot(path=screenshot_path, full_page=True)
            print(f"Screenshot saved to {screenshot_path}")

        except Exception as e:
            print(f"Error: {e}")
        finally:
            browser.close()

if __name__ == "__main__":
    verify_nav_removed()
