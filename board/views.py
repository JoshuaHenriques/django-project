from django.shortcuts import render
# Create your views here.


def index(request):
    posts = [
        {
            'id': '1',
            'title': 'Post title for some image',
            'content': 'this is a post content',
            'likes': 4,
            'comments': [
                {
                    'comment': 'this is the first comment'
                },
                {
                    'comment': 'this is the second comment'
                },
            ],
            'slug': 'first-post'
        },
        {
            'id': '2',
            'title': 'Post title for some another image',
            'content': 'this is a post content',
            'likes': 10,
            'comments': [
                {
                    'comment': 'this is the first comment'
                },
                {
                    'comment': 'this is the second comment'
                },
            ]
        },
        {
            'id': '3',
            'title': 'Post title for the last image',
            'content': 'this is a post content',
            'likes': 7,
            'comments': [
                {
                    'comment': 'this is the first comment'
                },
                {
                    'comment': 'this is the second comment'
                },
            ]
        },
    ]
    return render(request, 'board/index.html', {
        'show_board': True,
        'board_posts': posts
    })
    
def post_details(request, post_id):
	selected_post = {
		'id': '3',
		'title': 'Post title for the last image',
		'content': 'this is a post content',
		'likes': 7,
		'comments': [
			{
				'comment': 'this is the first comment'
			},
			{
				'comment': 'this is the second comment'
			},
		]
	}
	return render(request, 'board/post-details.html', {
		'post': selected_post
	})