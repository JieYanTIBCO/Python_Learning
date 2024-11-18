# 数据结构设计：列表 -> 字典 -> 字典 + 列表
social_media_data = [
    {
        'user_id': 'user_123',
        'posts': [
            {
                'title': 'My first post',
                'tags': ['python', 'coding'],
                'likes': 150,
                'comments': [
                    {'user': 'user_456', 'comment': 'Nice post!'},
                    {'user': 'user_789', 'comment': 'Thanks for sharing!'}
                ]
            },
            {
                'title': 'Another day in coding',
                'tags': ['life', 'tech'],
                'likes': 200,
                'comments': []
            }
        ]
    },
    {
        'user_id': 'user_456',
        'posts': [
            {
                'title': 'Hello world!',
                'tags': ['intro'],
                'likes': 50,
                'comments': [
                    {'user': 'user_123', 'comment': 'Welcome!'}
                ]
            }
        ]
    }
]

# 获取每个用户的总点赞数和评论数量：
for userdata in social_media_data:
    user_id=userdata['user_id']
    total_like=sum(post['likes'] for post in userdata['posts'])
    total_comment=sum(len(post['comments']) for post in userdata['posts'])


    # for post in userdata['posts']:
    #     sum_like+=post['likes']
    #     total_comment+=len(post['comments'])
    print(f"{user_id}:\n total like :{total_like}.\n  total comment:{total_comment}")