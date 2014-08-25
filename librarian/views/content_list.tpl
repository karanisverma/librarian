% rebase('base.tpl', title=_('Library'))
<h1>
{{ _('Library') }}
% if metadata:
<span>{{ str(ngettext('Showing %s of %s item', 'Showing %s of %s items', total_items)) % (len(metadata), total_items) }}</span>
% end
</h1>

<div class="inner">
    % if not metadata:
    <p>{{ _('Content library is currently empty') }}</p>
    % else:
    <form id="pager" class="pager controls">
        <p>
        % if total_pages > 1:
            <label for="page">page</label>
            <select id="page" name="p">
            % for i in range(1, total_pages + 1):
            <option value="{{ i }}"{{ i == page and ' selected' or '' }}>{{ i }}</option>
            % end
            </select>
            /
        % end
        <select id="perpage" name="c">
        % for i in range(1, 5):
        <option value="{{ i }}"{{ i == f_per_page and ' selected' or '' }}>{{ i * 20 }}</option>
        % end
        </select>
        <label for="perpage">per page</label>
        <button id="go-button" type="submit" class="special">{{ _('go') }}</button>
        </p>
    </form>
    <table class="content-list">
        <tr class="header">
        <th></th>
        <th>{{ _('title') }}</th>
        <th>{{ _('added') }}</th>
        </tr>
        % for meta in metadata:
        <tr>
        <td class="center">
            % if meta['favorite']:
            <img src="/static/img/fav.png" alt="favorite">
            % else:
            <form action="{{ i18n_path('/favorites/') }}" method="POST">
            {{! h.HIDDEN('md5', meta['md5']) }}
            <button type="submit">{{ _('favorite') }}</button>
            </form>
            % end
        </td>
        <td><a href="{{ i18n_path('/content/%s/' % meta['md5']) }}">{{ meta['title'] }}</a></td>
        <td>{{ meta['updated'].strftime('%m-%d') }}</td>
        </tr>
        % end
    </table>
    % end 
</div>

<script src="/static/js/jquery.js"></script>
<script src="/static/js/content.js"></script>
