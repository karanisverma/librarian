<%namespace name="widgets" file="../_widgets.tpl"/>

<% snr_pct = h.perc_range(status['snr'], 0, 1.6) %>
<% has_lock = h.yesno(status['has_lock'], status['signal'], _('No lock')) %>
<% has_service = h.yesno(has_lock and status['streams'] and status['streams'][0]['bitrate'], h.SPAN(_('Yes'), _class='has-lock'), h.SPAN(_('No'), _class='no-lock')) %>
## Translators, label is located next to the satellite signal strength indicator
${widgets.progress(_("Signal"), status['signal'], value=has_lock, threshold=50)}
## Translators, label is located next to the satellite signal quality indicator
${widgets.progress(_("Quality"), snr_pct, value=status['snr'], threshold=25)}

<p class="service">
    ## Translators, label shown before service lock indicator (e.g., Receiving data: yes)
    <span class="label">${_('Receiving data:')}</span> ${has_service}
</p>
<p class="bitrate">
    ## Translators, label shown before the current bitrate indicator (e.g., Bitrate: 68.7kbps)
    <span class="label">${_('Bitrate:')}</span> ${h.hsize(th.get_bitrate(status), unit='bps', step=1000)}
</p>
