from django.core.paginator import Paginator


class Page:
    def __init__(self, page_num, all_count, params,url_prefix, max_page=7, per_page=3):
        '''

        :param page_num: 当前页
        :param all_count: 数据总数量
        :param params: url参数列表
        :param max_page: 分页导航最大数量
        :param per_page: 每页数据条目
        :param url_prefix: url前缀
        '''
        self.url_prefix = url_prefix
        self.page_num = page_num
        self.all_count = all_count
        self.per_page = per_page
        self.max_page = max_page

        self.total_page, m = divmod(self.all_count, self.per_page)
        if m:
            self.total_page += 1

        if self.page_num:
            try:
                self.page_num = int(self.page_num)
                if self.page_num > self.total_page:
                    if self.total_page <= 0:
                        self.page_num = 1
                    else:
                        self.page_num = self.total_page
            except Exception as e:
                self.page_num = 1

        if self.total_page < self.max_page:
            self.max_page = self.total_page

        half_max_page = self.max_page // 2
        self.page_start = self.page_num - half_max_page
        self.page_end = self.page_num + half_max_page

        if self.page_start <= 1:
            self.page_start = 1
            self.page_end = self.max_page

        if self.page_end >= self.total_page:
            self.page_end = self.total_page
            self.page_start = self.total_page - self.max_page + 1

        import copy
        self.params = copy.copy(params)

        '''request.GET.urlencode()  将字典序列化  即转成 key=value&key1=value1..'''

        # print(self.params.urlencode())

    @property
    def start(self):
        return (self.page_num - 1) * self.per_page

    @property
    def end(self):
        return self.page_num * self.per_page

    def get_html(self):
        html_list = []

        self.params['page'] = 1
        html_list.append(f"<li><a href='{self.url_prefix}?{self.params.urlencode()}'>首页</a></li>")

        if self.page_num == 1:
            html_list.append('''
                <li class="disabled">
                    <a href="#" aria-label="Previous">
                        <span aria-hidden="true">&laquo;</span>
                    </a>
                </li>
                ''')
        else:
            self.params['page'] = self.page_num - 1
            html_list.append(f'''
                        <li>
                            <a href="{self.url_prefix}?{self.params.urlencode()}" aria-label="Previous">
                                <span aria-hidden="true">&laquo;</span>
                            </a>
                        </li>
                        ''')

        for i in range(self.page_start, self.page_end + 1):
            self.params['page'] = i
            if i == self.page_num:
                tmp = f"<li class='active'><a href='{self.url_prefix}?{self.params.urlencode()}'>{i}</a></li>"
            else:
                tmp = f"<li><a href='{self.url_prefix}?{self.params.urlencode()}'>{i}</a></li>"
            html_list.append(tmp)

        if self.page_num == self.total_page:
            html_list.append('''
                <li class="disabled">
                    <a href="#" aria-label="Previous">
                        <span aria-hidden="true">&raquo;</span>
                    </a>
                </li>
                ''')
        else:
            self.params['page'] = self.page_num + 1
            html_list.append(f'''
                        <li>
                            <a href="{self.url_prefix}?{self.params.urlencode()}" aria-label="Previous">
                                <span aria-hidden="true">&raquo;</span>
                            </a>
                        </li>
                        ''')

        self.params['page'] = self.total_page
        html_list.append(f"<li><a href='{self.url_prefix}?{self.params.urlencode()}'>尾页</a></li>")

        html_page = ''.join(html_list)

        return html_page
