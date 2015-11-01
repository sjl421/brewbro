from distutils.core import setup

setup(
	name="BrewBro",
	version="0.0.1",
	author="Fredrik Allansson",
	author_email="fredrik.allansson@gmail.com",
	packages=["brewbro"],
	include_package_data=True,
	url="https://github.com/skaggmannen/brewbro",
	description="A Brewing Web App",
	install_requires=[
		"sqlalchemy",
		"tornado",
	],
)
