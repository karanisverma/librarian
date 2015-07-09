<%inherit file='/base.tpl'/>

<%block name="title">
## Translators, used as page title
${_("How to Connect to Outernet")}
</%block>

<div class="products">
    <div class="h-bar narrower title">
        <h1 class="main">${_("How to connect")}</h1>
        <p>${_("Outernet datacasts over several frequencies, providing a few opportunities to receive our data. You can buy a receiver directly from us, make a receiver with a kit, or come up with your own way to connect.")}</p>
        <p>${_("Outernet is kind of like FM radio in this respect. We are happy to sell you our radios that receive the Outernet datacast, but our signal is unlocked and any compatible receiver will work. If you develop a receiver that is cheaper or better than ours, we will help you sell it.")}</p>
        <p>${_("Remember, once you have a receiver, the datacast is completely free.")}</p>
    </div>

    <div class="pic-row">
        <div class="pic-col lantern"></div>
    </div>

    <div class="h-bar narrower white lantern">
        <h3>${_("Lantern (by Outernet)")}</h3>
        <p class="description">${_("Lantern is one of the most versatile information tools on Earth. Lantern receives Outernet’s free datacast anywhere on Earth with its internal antennae. Lantern also sports an internal battery and solar panel to allow for remote charging of itself and a phone or tablet.")}</p>
        <p class="overview">
            <label class="quantity"><span class="icon"></span>${_("1 Item")}</label>
            <label class="price"><span class="icon"></span>${_("$169")}</label>
        </p>
        <p class="buttons">
            <a class="button cta primary" href="https://www.indiegogo.com/projects/lantern-one-device-free-data-from-space-forever">
                <span class="buy">
                    <span class="icon"></span>
                    <span class="label">${_("Reserve Your Lantern")}</span>
                </span>
            </a>
        </p>
    </div>

    <div class="pic-row">
        <div class="pic-col pillar"></div>
    </div>

    <div class="h-bar narrower white pillar">
        <h3>${_("Lighthouse (by Outernet)")}</h3>
        <p class="description">${_("Lighthouse is like a Wi-Fi router that does not require an Internet connection. Instead, Lighthouse connects to a satellite dish and receives Outernet’s free datacast. Lighthouse stores the files it receives from Outernet on its drive (expandable via three USB slots) that users connect to over Wi-Fi.")}</p>
        <p class="overview">
            <label class="quantity"><span class="icon"></span>${_("2 Items")}</label>
            <label class="price"><span class="icon"></span>${_("$99")}</label>
        </p>
        <p class="buttons">
            <a class="button cta primary" href="http://store.outernet.is/">
                <span class="buy">
                    <span class="icon"></span>
                    <span class="label">${_("Buy Your Lighthouse")}</span>
                </span>
            </a>
            <a class="button" href="https://wiki.outernet.is/">${_("More information")}</a>
        </p>
    </div>

    <div class="pic-row">
        <div class="pic-col diy"></div>
    </div>

    <div class="h-bar narrower white diy">
        <h3>${_("Build Your Own Receiver")}</h3>
        <p class="description">${_("With Outernet, it is truly possible for anyone to build their own digital library. Using a Raspberry Pi and some other off the shelf components, you can build your own Lighthouse. One of the components even lets you get free satellite TV! Buy a full kit or just the pieces you need.")}</p>
        <p class="overview">
            <label class="quantity"><span class="icon"></span>${_("5+ Items")}</label>
            <label class="price"><span class="icon"></span>${_("$35 - $135")}</label>
        </p>
        <p class="buttons">
            <a class="button cta primary" href="http://store.outernet.is/">
                <span class="buy">
                    <span class="icon"></span>
                    <span class="label">${_("Buy Your Outernet Kit")}</span>
                </span>
            </a>
        </p>
        <p class="description">${_("Outernet uses Free to Air television signals that are unlocked all over the world. If you find a tuner that works with a Raspberry Pi or another type of computer, let us know! We encourage the community to experiment with tuners, drivers, and computer modules and make something better than what we have. Consider the challenge issued.")}</p>
    </div>
</div>
