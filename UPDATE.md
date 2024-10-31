[31-10-2024]
**Update Summary for OpenEdit Editor v1.1**

1. **File Handling:**
   - Added **support for C++ and Java files** in `filedialog.asksaveasfilename` within the `save_file` function.

2. **Open File Confirmation:**
   - Removed the confirmation dialog in `open_file` that asked about unsaved changes when opening a new file.

3. **Theme Toggle:**
   - Expanded **theme color schemes** with additional light and dark theme customization:
     - **Light Theme**: Background colors for the window, text editor, line numbers, button frame, and all buttons.
     - **Dark Theme**: Modified background and foreground colors for better readability in dark mode.
   - Added background and foreground color adjustments for each button according to the selected theme.
   - Renamed the theme tracking variable `dark_theme` to `is_dark_theme`.

4. **Text Size Adjustment:**
   - Reduced text size range to **8-25** in `adjust_text_size`, narrowing customization.
   - Changed font style from "Terminal" to "Courier" for text editing and line numbers.

5. **Cursor Properties:**
   - Modified `insertwidth` to **2** and adjusted `insertontime/insertofftime` to **300ms**, refining cursor blink for user preference.

6. **Button Layout and Configuration:**
   - **Removed `padx` for individual buttons**, simplifying layout spacing.

7. **Line Index Feature:**
   - Added a **line index display area** on the left side of the text editor, showing line numbers for easy navigation.

8. **Key Bindings:**
   - Updated comments to clarify optional keyboard shortcuts, specifically mentioning `<Control-n>` for a new file.

9. **Global Variable Initialization:**
   - Grouped `global` variables for consistency and readability.

10. **Code Commenting and Formatting:**
    - Added detailed color explanations within the theme toggle function, supporting customization and clarity.
