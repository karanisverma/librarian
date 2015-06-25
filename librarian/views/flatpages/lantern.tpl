<%inherit file='/base.tpl'/>
<%namespace name='library_submenu' file='/_library_submenu.tpl'/>

<%block name="title">
## Translators, used as page title
${_("Lantern")}
</%block>

${library_submenu.body()}

<div class="products">
    <div class="h-bar narrower title lantern">
        <h1 class="main">${_("Lantern (by Outernet)")}</h1>
        <p class="description">${_("Lorem ipsum dolor sit amet, consectetur adipiscing elit. Integer nec odio. Praesent libero. Sed cursus ante dapibus diam. Sed nisi. Nulla quis sem at nibh elementum imperdiet. Duis sagittis ipsum. Praesent mauris. Fusce nec tellus sed augue semper porta. Mauris massa. Vestibulum lacinia arcu eget nulla. Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos. Curabitur sodales ligula in libero. Sed dignissim lacinia nunc.")}</p>
        <p class="overview">
            <label class="quantity"><span class="icon"></span>${_("1 item")}</label>
            <label class="time"><span class="icon"></span>${_("10 minutes")}</label>
            <label class="price"><span class="icon"></span>${_("$70")}</label>
        </p>
    </div>

    <div class="pic-row">
        <div class="pic-col lantern"></div>
    </div>

    <div class="h-bar narrower white details">
        <h3>${_("Essentials")}</h3>
        <p class="description">${_("Duis sagittis ipsum. Praesent mauris. Fusce nec tellus sed augue semper porta. Mauris massa. Vestibulum lacinia arcu eget nulla. Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos.")}</p>
        <p class="items">
            <span class="name">${_("Lantern")}</span>
            <a class="buy" href="javascript:;">${_("Buy now")} <span class="icon"></span></a>
        </p>
        <hr />
        <p class="items">
            <span class="name">${_("Wi-Fi device")}</span>
        </p>
        <h3>${_("Optional")}</h3>
        <p class="items">
            <span class="name">${_("Satellite dish (60cm)")}</span>
            <a class="buy" href="javascript:;">${_("Buy now")} <span class="icon"></span></a>
        </p>
    </div>

    <div class="h-bar" id="step-1">
        <h3>${_("Step 1. Turn on your Lantern")}</h3>
        <table>
            <tr>
                <td>
                    <label>${_("1.1 Lorem ipsum")}</label>
                    <p>${_("Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur.")}</p>
                </td>
                <td>
                    <label>${_("1.2 Lorem ipsum")}</label>
                    <p>${_("Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur.")}</p>
                </td>
                <td>
                    <label>${_("1.3 Lorem ipsum")}</label>
                    <p>${_("Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur.")}</p>
                </td>
                <td>
                    <label>${_("1.4 Lorem ipsum")}</label>
                    <p>${_("Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur.")}</p>
                </td>
            </tr>
            <tr>
                <td colspan="2">
                    <label><span class="optional">${_("Optional!")}</span> ${_("1.5 Lorem ipsum")}</label>
                    <p>${_("Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur.")}</p>
                </td>
                <td>
                    <label>${_("1.6 Lorem ipsum")}</label>
                    <p>${_("Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur.")}</p>
                </td>
                <td>
                    <label>${_("1.7 Lorem ipsum")}</label>
                    <p>${_("Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur.")}</p>
                </td>
            </tr>
        </table>

        <div class="switch dish-switch">
            <a href="#step3" class="left no-dish">
                <span class="icon"></span>
                ${_("No optional dish")}
            </a>
            <span class="right active have-dish">
                <span class="icon"></span>
                ${_("I have an optional dish")}
            </span>
        </div>
    </div>

    <div class="h-bar white" id="step-2">
        <h3>${_("Step 2. Point your dish")}</h3>
        <p class="description narrower">${_("Duis sagittis ipsum. Praesent mauris. Fusce nec tellus sed augue semper porta. Mauris massa. Vestibulum lacinia arcu eget nulla. Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos.")}</p>
        <table>
            <tr>
                <th>${_("Region")}</th>
                <th>${_("Satellite")}</th>
                <th>${_("Frequency")}</th>
                <th>${_("Symbol rate")}</th>
                <th>${_("FEC")}</th>
                <th>${_("Polarization")}</th>
            </tr>
            <tr>
                <td>North America (US & Canada)</td>
                <td><a href="javascript:;">Galaxy 19 97.0&deg; W</a></td>
                <td>12177000 kHz</td>
                <td>27500000 baud</td>
                <td>3/4</td>
                <td>${_("Vertical")}</td>
            </tr>
            <tr>
                <td>Europe, Africa</td>
                <td><a href="javascript:;">Intelsat 10 47.5&deg; E</a></td>
                <td>12177000 kHz</td>
                <td>27500000 baud</td>
                <td>3/4</td>
                <td>${_("Vertical")}</td>
            </tr>
            <tr>
                <td>Europe & North Africa</td>
                <td><a href="javascript:;">Hotbird 13.0&deg; E</a></td>
                <td>12177000 kHz</td>
                <td>27500000 baud</td>
                <td>3/4</td>
                <td>${_("Vertical")}</td>
            </tr>
            <tr>
                <td>Europe & Sub-Saharan Africa</td>
                <td><a href="javascript:;">Intelsat 20 68.5&deg; E</a></td>
                <td>12177000 kHz</td>
                <td>27500000 baud</td>
                <td>3/4</td>
                <td>${_("Vertical")}</td>
            </tr>
            <tr>
                <td>Asia</td>
                <td><a href="javascript:;">AsiaSat 5 C-band 100.5&deg; E</a></td>
                <td>12177000 kHz</td>
                <td>27500000 baud</td>
                <td>3/4</td>
                <td>${_("Vertical")}</td>
            </tr>
        </table>
        <a class="button primary more-info" href="javascript:;">${_("More information at GitHub")}</a>
    </div>

    <div class="h-bar narrower" id="step-3">
        <h3>${_("Step 3. Access Librarian")}</h3>
        <p class="description">${_("Duis sagittis ipsum. Praesent mauris. Fusce nec tellus sed augue semper porta. Mauris massa. Vestibulum lacinia arcu eget nulla. Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos.")}</p>
    </div>

    <div class="h-bar white narrower" id="step-4">
        <h3>${_("Step 4. Etcetera")}</h3>
        <p class="description">${_("Duis sagittis ipsum. Praesent mauris. Fusce nec tellus sed augue semper porta. Mauris massa. Vestibulum lacinia arcu eget nulla. Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos.")}</p>
    </div>

    <div class="h-bar narrower complete">
        <span class="icon"></span>
        <h3>${_("Great job! You're all done.")}</h3>
    </div>

</div>
