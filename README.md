# Main Website


The goal of this project is to redesign the _main_ _Linux Mint website._

## Scope :

- We only care about the landing page for now.
- We only work with static content (HTML/CSS, no server backend).

## Themes


In this project we modify a theme called Wizixo.

**Pros:**

- Great block separators, easy to use
- Gradients and geometrical shapes
- Perfect color palette

**Cons:**

- Fonts (small, pale, roboto..)

## Structure

- `wizixo/documentation` contains the theme documentation.
- `wizixo/template` contains the root of the mint website. This is **where we work.**
- `wizixo/*` contains the gulp file to regenerate the assets.

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
            <td>Home</td>
            <td>Home page</td>
            <td>mint-main.html</td>
            <td>Describes what Mint is, why it's good, to newcomers.</td>
        </tr>
        <tr>
            <td rowspan=3>Download</td>
            <td>Linux Mint 20.2</td>
            <td>mint-download.html</td>
            <td>Same as old website</td>
        </tr>
        <tr>
            <td>LMDE 4</td>
            <td>mint-download-lmde.html</td>
            <td>Same as old website</td>
        </tr>
        <tr>
            <td>All versions</td>
            <td>mint-download-all.html</td>
            <td>Same as old website</td>
        </tr>
        <tr>
            <td rowspan=7>Project</td>
            <td>Donors</td>
            <td>mint-donors.html</td>
            <td>Same as old website</td>
        </tr>
        <tr>
            <td>Sponsors</td>
            <td>mint-sponsors.html</td>
            <td>Same as old website</td>
        </tr>
        <tr>
            <td>Partners</td>
            <td>mint-partners.html</td>
            <td>Same as old website</td>
        </tr>
        <tr>
            <td>Store</td>
            <td>mint-store.html</td>
            <td>Same as old website</td>
        </tr>
        <tr>
            <td>Get Involved</td>
            <td>mint-get-involved.html</td>
            <td>Same as old website</td>
        </tr>
        <tr>
            <td>Development</td>
            <td>mint-development.html</td>
            <td>Describes our projects (replaces https://projects.linuxmint.com/) </td>
        </tr>
        <tr>
            <td>Mirrors</td>
            <td>mint-mirrors.html</td>
            <td>Same as old website</td>
        </tr>
      <tr>
            <td rowspan=8>About</td>
            <td>About Linux Mint</td>
            <td>mint-about.html</td>
            <td>Describes the OS and the project more in details.</td>
        </tr>
        <tr>
            <td>FAQ</td>
            <td>mint-faq.html</td>
            <td>Accordion style? Answer main questions people have.</td>
        </tr>
        <tr>
            <td>Documentation</td>
            <td>mint-documentation.html</td>
            <td>Should really push people towards the main documents rather than just list all of them in a table.</td>
        </tr>
        <tr>
            <td>Screenshots</td>
            <td>mint-screenshots.html</td>
            <td>Same as old website</td>
        </tr>
        <tr>
            <td>Team</td>
            <td>mint-team.html</td>
            <td>Same as old website</td>
        </tr>
        <tr>
            <td>Contact</td>
            <td>mint-contact.html</td>
            <td>Same as old website</td>
        </tr>
        <tr>
            <td>Privacy and Cookies</td>
            <td>mint-privacy.html</td>
            <td>Same as old website</td>
        </tr>
        <tr>
            <td>Brand</td>
            <td>mint-brand.html</td>
            <td>Should provide resources for using our brand (logo, name..etc), explain what is OK and what isn't, explain what people can do with Linux Mint without the need to ask for permission etc...</td>
        </tr>
      <tr>
            <td rowspan=1>Links</td>
            <td>Local Communities</td>
            <td>mint-communities.html</td>
            <td>Same as old website</td>
        </tr>
    </tbody>
</table>

# Getting Started :

### Fork this repository and then clone it locally using gitbash or terminal if you are on Linux or macos


##  Open your terminal or vs-code terminal and type the following 

```
cd website-wizixo/wizixo/template
code .
firefox mint-main.html (Only for linux-users)
```
### You can open the mint-main.html page easily in your browser by opening the **mint-main.html** file .

