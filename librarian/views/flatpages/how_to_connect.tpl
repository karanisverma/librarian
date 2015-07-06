<%inherit file='/base.tpl'/>
<%namespace name='library_submenu' file='/_library_submenu.tpl'/>

<%block name="title">
## Translators, used as page title
${_("How to connect")}
</%block>

${library_submenu.body()}

<div class="products">
    <div class="h-bar narrower title">
        <h1 class="main">${_("How to connect")}</h1>
        <h3 class="sub">${_("Do you already have a device that lorem ipsum?")}</h3>
        <p>${_("Lorem ipsum dolor sit amet, his ei libris accusam quaerendum, falli doctus senserit per id, eos et exerci atomorum instructior. Ex eum essent cotidieque, te eum tritani adversarium.")}</p>
        <p class="buttons">
            <a class="button" href="javascript:;">${_("Yes")}</a>
            <a class="button" href="javascript:;">${_("No")}</a>
        </p>
    </div>

    <div class="pic-row">
        <div class="pic-col lantern"></div>
    </div>

    <div class="h-bar narrower white lantern">
        <h3>${_("Lantern (by Outernet)")}</h3>
        <p class="description">${_("Lorem ipsum dolor sit amet, consectetur adipiscing elit. Integer nec odio. Praesent libero. Sed cursus ante dapibus diam. Sed nisi. Nulla quis sem at nibh elementum imperdiet. Duis sagittis ipsum. Praesent mauris. Fusce nec tellus sed augue semper porta. Mauris massa. Vestibulum lacinia arcu eget nulla. Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos. Curabitur sodales ligula in libero. Sed dignissim lacinia nunc.")}</p>
        <p class="overview">
            <label class="quantity"><span class="icon"></span>${_("1 item")}</label>
            <label class="time"><span class="icon"></span>${_("10 minutes")}</label>
            <label class="price"><span class="icon"></span>${_("$70")}</label>
        </p>
        <p class="buttons">
            <a class="button cta primary" href="javascript:;">
                <span class="buy">
                    <span class="icon"></span>
                    <span class="label">${_("Buy the Lantern")}</span>
                </span>
            </a>
            <a class="button" href="javascript:;">${_("Read the easy 2 step set-up")}</a>
        </p>
    </div>

    <div class="pic-row">
        <div class="pic-col pillar"></div>
    </div>

    <div class="h-bar narrower white pillar">
        <h3>${_("Pillar (by Outernet)")}</h3>
        <p class="description">${_("Lorem ipsum dolor sit amet, consectetur adipiscing elit. Integer nec odio. Praesent libero. Sed cursus ante dapibus diam. Sed nisi. Nulla quis sem at nibh elementum imperdiet. Duis sagittis ipsum. Praesent mauris. Fusce nec tellus sed augue semper porta. Mauris massa. Vestibulum lacinia arcu eget nulla. Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos. Curabitur sodales ligula in libero. Sed dignissim lacinia nunc.")}</p>
        <p class="overview">
            <label class="quantity"><span class="icon"></span>${_("1 item")}</label>
            <label class="time"><span class="icon"></span>${_("3 minutes")}</label>
            <label class="price"><span class="icon"></span>${_("$100")}</label>
        </p>
        <p class="buttons">
            <a class="button cta primary" href="javascript:;">
                <span class="buy">
                    <span class="icon"></span>
                    <span class="label">${_("Buy the Pillar")}</span>
                </span>
            </a>
            <a class="button" href="javascript:;">${_("Read the easy 3 step set-up")}</a>
        </p>
    </div>

    <div class="pic-row">
        <div class="pic-col diy"></div>
    </div>

    <div class="h-bar narrower white diy">
        <h3>${_("Build your own receiver")}</h3>
        <p class="description">${_("Lorem ipsum dolor sit amet, consectetur adipiscing elit. Integer nec odio. Praesent libero. Sed cursus ante dapibus diam. Sed nisi. Nulla quis sem at nibh elementum imperdiet. Duis sagittis ipsum. Praesent mauris. Fusce nec tellus sed augue semper porta. Mauris massa. Vestibulum lacinia arcu eget nulla. Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos. Curabitur sodales ligula in libero. Sed dignissim lacinia nunc.")}</p>
        <p class="overview">
            <label class="quantity"><span class="icon"></span>${_("11 - 24 items")}</label>
            <label class="time"><span class="icon"></span>${_("45 - 90 minutes")}</label>
            <label class="price"><span class="icon"></span>${_("$75 - $150")}</label>
        </p>
        <p class="buttons">
            <a class="button cta primary" href="javascript:;">
                <span class="buy">
                    <span class="icon"></span>
                    <span class="label">${_("Buy a Kit")}</span>
                </span>
            </a>
            <a class="button" href="javascript:;">${_("Read the easy 3 step set-up")}</a>
        </p>
    </div>

    <div class="pic-row">
        <div class="pic-col usb-stb"></div>
    </div>

    <div class="h-bar narrower white usb-stb">
        <h3>${_("USB set top box")}</h3>
        <p class="description">${_("Lorem ipsum dolor sit amet, consectetur adipiscing elit. Integer nec odio. Praesent libero. Sed cursus ante dapibus diam. Sed nisi. Nulla quis sem at nibh elementum imperdiet. Duis sagittis ipsum. Praesent mauris. Fusce nec tellus sed augue semper porta. Mauris massa. Vestibulum lacinia arcu eget nulla. Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos. Curabitur sodales ligula in libero. Sed dignissim lacinia nunc.")}</p>
        <p class="overview">
            <label class="quantity"><span class="icon"></span>${_("5 items")}</label>
            <label class="time"><span class="icon"></span>${_("10 minutes")}</label>
            <label class="price"><span class="icon"></span>${_("$50 - $100")}</label>
        </p>
        <p class="buttons">
            <a class="button cta primary" href="javascript:;">
                <span class="buy">
                    <span class="icon"></span>
                    <span class="label">${_("Buy a set top box")}</span>
                </span>
            </a>
            <a class="button" href="javascript:;">${_("Read the 5 step set-up")}</a>
        </p>
    </div>
</div>
