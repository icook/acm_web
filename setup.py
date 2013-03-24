from distutils.core import setup

setup(
    name='kuacm',
    version='0.1',
    author=u'Isaac Cook',
    author_email='isaac@simpload.com',
    packages=['org_web', 'acm_site'],
    install_requires=['django==1.4','south', 'pil'],
    license='BSD licence, see LICENCE.txt',
    description='Simple website for University of Kansas Association for Computing Machinery Chapter',
    zip_safe=False,
)
