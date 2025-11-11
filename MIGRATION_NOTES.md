# Hugo PaperMod Theme Migration - November 11, 2025

## Summary

Successfully migrated from outdated bootstrap-premium theme to PaperMod theme (academic variant based on Pascal Michaillat's template).

## What Was Done

### 1. Backups Created
- `config.toml.bak` - Original configuration
- `netlify.toml.bak` - Original Netlify config
- `themes/bootstrap-premium.bak/` - Old theme
- `layouts.bak/` - Old custom layouts

### 2. Theme Installation
- Installed PaperMod theme as git submodule at `themes/PaperMod/`
- Command: `git submodule add --depth=1 https://github.com/adityatelange/hugo-PaperMod.git themes/PaperMod`

### 3. Configuration Updates

#### New hugo.toml
- Converted from config.toml to hugo.toml (modern format)
- Updated pagination config (deprecated `paginate` → `pagination.pagerSize`)
- Enabled profileMode for academic homepage
- Added profile buttons for Research, Teaching, Blog, Resources, CV
- Configured social icons (email, github, twitter, mastodon, rss)
- Set up main menu structure
- Enabled KaTeX for math rendering
- Configured custom CSS path

#### Updated netlify.toml
- Hugo version: 0.47.1 → 0.139.3
- Updated build command to use modern flags: `hugo --gc --minify`
- Kept all existing redirects intact

### 4. Content Structure Updates
- Created `content/_index.md` for homepage
- Removed duplicate menu entries from content files' frontmatter:
  - contact.md
  - research.md
  - teaching.md
  - resources.md
- Menu now defined centrally in hugo.toml

### 5. Custom CSS Migration
- Created `assets/css/extended/custom.css`
- Preserved key styling preferences:
  - Custom color scheme (blue navbar, cream background)
  - Typography (Helvetica, Avenir with small-caps)
  - Link styling (dotted underlines)
  - Text justification
- PaperMod's `extended` directory allows custom CSS without modifying theme files

### 6. Removed Old Theme Files
- Moved old `layouts/` directory to `layouts.bak/`
- Old theme layouts were causing conflicts with PaperMod

## Build Status

✅ Site builds successfully with no errors
✅ Hugo v0.152.2 confirmed working
✅ Local dev server tested and functional

## ox-hugo Compatibility

✅ No changes needed to your org-mode workflow
✅ ox-hugo continues to export to standard Hugo markdown
✅ All existing content files remain compatible

## What You Need To Do

### 1. Review Local Site
```bash
hugo server
# Visit http://localhost:1313
```

### 2. Check Styling
- Review the profile page buttons and layout
- Verify custom CSS is working as expected
- Test mobile responsiveness
- Check that all pages render correctly

### 3. Update CV Files
- Ensure `/materials/McLearCV.pdf` exists
- Consider adding HTML version if desired

### 4. Update Contact Info
The contact.md file still references:
- UNL office location
- Old email (mclear@unl.edu)
- Office hours

You may want to update this to reflect your current status.

### 5. Update Home Page Content
The profileMode subtitle in hugo.toml contains your bio. You may want to:
- Update the text to reflect current status
- Adjust the profile buttons
- Add a profile image if desired

### 6. Git Workflow

When ready to deploy:

```bash
# Stage all changes
git add .

# Commit the migration
git commit -m "Migrate to PaperMod theme

- Replace bootstrap-premium with PaperMod
- Update Hugo config to modern format
- Update Netlify Hugo version to 0.139.3
- Migrate custom CSS to extended directory
- Clean up duplicate menu entries"

# Push to trigger Netlify deployment
git push origin master
```

## Optional Enhancements

### Add Profile Image
1. Add image to `static/` directory (e.g., `static/profile.jpg`)
2. Update hugo.toml:
   ```toml
   [params.profileMode]
   imageUrl = '/profile.jpg'
   imageWidth = 120
   imageHeight = 120
   ```

### Customize Colors
Edit `assets/css/extended/custom.css` to adjust:
- Color scheme in `:root` CSS variables
- Font choices
- Link styling
- Spacing

### Add Search
PaperMod supports search. Add to hugo.toml:
```toml
[outputs]
home = ['HTML', 'RSS', 'JSON']
```
Then create search page if desired.

## Troubleshooting

### If Hugo Build Fails
1. Check Hugo version: `hugo version`
2. Should be v0.139.3+ for production
3. Clear cache: `hugo --gc`

### If CSS Not Loading
1. Verify path: `assets/css/extended/custom.css`
2. Check hugo.toml has correct assets.css reference
3. Clear browser cache

### If Content Not Appearing
1. Check frontmatter in content files
2. Verify `draft = false` in frontmatter
3. Check menu configuration in hugo.toml

## Resources

- [PaperMod Documentation](https://adityatelange.github.io/hugo-PaperMod/)
- [PaperMod GitHub](https://github.com/adityatelange/hugo-PaperMod)
- [Michaillat Academic Template](https://pascalmichaillat.org/b/)
- [Hugo Documentation](https://gohugo.io/documentation/)

## File Locations Reference

```
website/
├── hugo.toml                          # Main config (NEW)
├── config.toml.bak                    # Old config backup
├── netlify.toml                       # Updated for new Hugo
├── netlify.toml.bak                   # Backup
├── assets/
│   └── css/
│       └── extended/
│           └── custom.css             # Custom styling
├── content/
│   ├── _index.md                      # Homepage (NEW)
│   ├── contact.md                     # Updated
│   ├── research.md                    # Updated
│   ├── teaching.md                    # Updated
│   ├── resources.md                   # Updated
│   └── posts/                         # Blog posts (unchanged)
├── themes/
│   ├── PaperMod/                      # New theme (submodule)
│   └── bootstrap-premium.bak/         # Old theme backup
├── layouts.bak/                       # Old layouts backup
└── static/                            # Static assets (unchanged)
```
