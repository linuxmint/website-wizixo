# Main Website

<p align="center">
  <img src="./img/logo.svg" height="100" style="border-radius: 6px" />
</p>

<p align="center">
<img alt="Slack" src="https://img.shields.io/badge/Slack-4A154B?style=for-the-badge&logo=slack&logoColor=white"/>
<img alt="Html5" src="https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white"/>
<img alt="Css3" src="https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white"/>
<img alt="Javascript" src="https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black"/>
</p>

<hr>

The goal of this project is to redesign the main Linux Mint website.

## Scope

- We only care about the landing page for now.
- We only work with static content (HTML/CSS, no server backend).

## Themes

In this project we modify a theme called Wizixo.

Pros:

- Great block separators, easy to use
- Gradients and geometrical shapes
- Perfect color palette

Cons:

- Fonts (small, pale, roboto..)

## Structure

- `wizixo/documentation` contains the theme documentation.
- `wizixo/template` contains the root of the mint website. This is where we work.
- `wizixo/*` contains the gulp file to regenerate the assets.
- `wizixo/template/mint-section-*.html` contain HTML/CSS sections which are used in multiple pages.
- `wizixo/template/mint-page-*.html` are the source for Mint pages. They can contain `<include>` tags to include common sections which are replaced using `build.py`.
- `wizixo/build.py` is a script which builds the Mint pages.

## Install and running

Clone the project:

```bash
git clone https://github.com/linuxmint/website-wizixo.git
```

Navigate to project folder:

```bash
cd website-wizixo/wizixo
```

Navigate to the `wizixo` folder and install the dependencies:

```bash
npm install
#or
yarn
```

Now, build the pages:

```bash
yarn build
# or you can run the build.py file on root folder
```

Run the local server:

```bash
npm start
#or
yarn start
```

(ou can use others local http servers like: live server or python http.server)

## Building pages

To avoid duplicating the same headers and footers in every single page, we put common sections in `mint-section-*.html` files.

We then work on pages called `mint-page-*.html` which include these sections with `<include>` tags.

Let's take an example:

- `mint-page-privacy.html` is the page we work on, it's in our git tree.
- It contains three tags to include the header, title and the footer: `<include src="mint-section-header.html"/>`, `<include src="mint-section-title.html" title="Privacy"/>` and `<include src="mint-section-footer.html"/>`
- When we run `build.py`, it generates `mint-privacy.html` using the content of `mint-page-privacy.html` and it replaces the `include` tags with the content of the header and footer sections.

Note that with the exception of `src`, attributes are also used. In the example above, `title="Privacy` is used to replace `$title` with `Privacy` when injecting the content of `mint-section-title.html`.

The resulting `mint-privacy.html` page is what we can open with our Web browser.

## Web pages

<table>
    <thead>
        <tr>
            <th>Category</th>
            <th>Page</th>
            <th>Filename</th>
            <th>Notes</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td rowspan=3>Common sections</td>
            <td>Header</td>
            <td>mint-section-header.html</td>
            <td>HTML head, body all the way down to the menu (included).</td>
        </tr>
        <tr>
            <td>Footer</td>
            <td>mint-section-footer.html</td>
            <td>Footer section.</td>
        </tr>
        <tr>
            <td>Title</td>
            <td>mint-section-title.html</td>
            <td>Title section, used at the top of the page in all pages, except the main page.</td>
        </tr>
        <tr>
            <td>Sponsors footer</td>
            <td>mint-section-sponsors.tml</td>
            <td>A sponsor section just above the footer, on all pages except the sponsors, partners and home pages.</td>
        </tr>
        <tr>
            <td>Home</td>
            <td>Home page</td>
            <td>mint-page-main.html</td>
            <td>Describes what Mint is, why it's good, to newcomers.</td>
        </tr>
        <tr>
            <td rowspan=7>Download</td>
            <td>Linux Mint 20.2</td>
            <td>mint-page-download.html</td>
            <td>Same as old website</td>
        </tr>
        <tr>
            <td>LMDE 4</td>
            <td>mint-page-download-lmde.html</td>
            <td>Same as old website</td>
        </tr>
        <tr>
            <td>All versions</td>
            <td>mint-page-download-all.html</td>
            <td>Same as old website</td>
        </tr>
        <tr>
            <td>Edition</td>
            <td>mint-page-edition.html</td>
            <td>Same as old website, download links with mirrors for a particular edition</td>
        </tr>
        <tr>
            <td>Release notes</td>
            <td>mint-page-notes.html</td>
            <td>Same as old website</td>
        </tr>
        <tr>
            <td>New features</td>
            <td>mint-page-features.html</td>
            <td>Same as old website</td>
        </tr>
        <tr>
            <td>Verify</td>
            <td>mint-page-verify.html</td>
            <td>Same as old website</td>
        </tr>
        <tr>
            <td rowspan=7>Project</td>
            <td>Donors</td>
            <td>mint-page-donors.html</td>
            <td>Same as old website</td>
        </tr>
        <tr>
            <td>Sponsors</td>
            <td>mint-page-sponsors.html</td>
            <td>Same as old website</td>
        </tr>
        <tr>
            <td>Partners</td>
            <td>mint-page-partners.html</td>
            <td>Same as old website</td>
        </tr>
        <tr>
            <td>Store</td>
            <td>mint-page-store.html</td>
            <td>Same as old website</td>
        </tr>
        <tr>
            <td>Get Involved</td>
            <td>mint-page-get-involved.html</td>
            <td>Same as old website</td>
        </tr>
        <tr>
            <td>Development</td>
            <td>mint-page-development.html</td>
            <td>Describes our projects (replaces https://projects.linuxmint.com/) </td>
        </tr>
        <tr>
            <td>Mirrors</td>
            <td>mint-page-mirrors.html</td>
            <td>Same as old website</td>
        </tr>
      <tr>
            <td rowspan=8>About</td>
            <td>About Linux Mint</td>
            <td>mint-page-about.html</td>
            <td>Describes the OS and the project more in details.</td>
        </tr>
        <tr>
            <td>FAQ</td>
            <td>mint-page-faq.html</td>
            <td>Accordion style? Answer main questions people have.</td>
        </tr>
        <tr>
            <td>Documentation</td>
            <td>mint-page-documentation.html</td>
            <td>Should really push people towards the main documents rather than just list all of them in a table.</td>
        </tr>
        <tr>
            <td>Screenshots</td>
            <td>mint-page-screenshots.html</td>
            <td>Same as old website</td>
        </tr>
        <tr>
            <td>Team</td>
            <td>mint-page-team.html</td>
            <td>Same as old website</td>
        </tr>
        <tr>
            <td>Contact</td>
            <td>mint-page-contact.html</td>
            <td>Same as old website</td>
        </tr>
        <tr>
            <td>Privacy and Cookies</td>
            <td>mint-page-privacy.html</td>
            <td>Same as old website</td>
        </tr>
        <tr>
            <td>Brand</td>
            <td>mint-page-brand.html</td>
            <td>Should provide resources for using our brand (logo, name..etc), explain what is OK and what isn't, explain what people can do with Linux Mint without the need to ask for permission etc...</td>
        </tr>
      <tr>
            <td rowspan=1>Links</td>
            <td>Local Communities</td>
            <td>mint-page-communities.html</td>
            <td>Same as old website</td>
        </tr>
    </tbody>
</table>

<div align="center">

 <img src="./wizixo/template/img/favicon.ico" height="50" style="border-radius: 6px" />

</div>
