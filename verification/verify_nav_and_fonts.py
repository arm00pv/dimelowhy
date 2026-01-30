from playwright.sync_api import sync_playwright, expect

def verify_nav_and_fonts():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        try:
            page.goto("http://localhost:8000")

            # Verify Nav
            nav = page.locator("#nav")
            expect(nav).to_be_visible()

            # Check for "Servicios" link
            servicios_link = page.locator("#nav ul li:has-text('Servicios')")
            expect(servicios_link).to_be_visible()

            # Check for "Artistas" dropdown
            artistas_link = page.locator("#nav ul li:has-text('Artistas')")
            expect(artistas_link).to_be_visible()

            # Hover over Artistas to see submenu
            artistas_link.hover()
            # Wait a bit for transition if any
            page.wait_for_timeout(500)

            # Take screenshot
            screenshot_path = "/home/jules/verification/verification.png"
            page.screenshot(path=screenshot_path, full_page=True)
            print(f"Screenshot saved to {screenshot_path}")

        except Exception as e:
            print(f"Error: {e}")
        finally:
            browser.close()

if __name__ == "__main__":
    verify_nav_and_fonts()
