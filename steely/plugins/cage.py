'''our one true god'''


import random


__author__ = 'sentriz'
COMMAND = 'nick'
NICKS = (
    "https://upload.wikimedia.org/wikipedia/commons/thumb/3/33/Nicolas_Cage_2011_CC.jpg/220px-Nicolas_Cage_2011_CC.jpg",
    "https://upload.wikimedia.org/wikipedia/commons/thumb/f/f3/Nicolas_Cage_-_66%C3%A8me_Festival_de_Venise_%28Mostra%29.jpg/220px-Nicolas_Cage_-_66%C3%A8me_Festival_de_Venise_%28Mostra%29.jpg",
    "https://images-na.ssl-images-amazon.com/images/M/MV5BMTUzMDM4Nzk2MV5BMl5BanBnXkFtZTcwNTcwNjExOQ@@._V1_UY317_CR1,0,214,317_AL_.jpg",
    "https://upload.wikimedia.org/wikipedia/commons/thumb/c/c0/Nicolas_Cage_Deauville_2013.jpg/220px-Nicolas_Cage_Deauville_2013.jpg",
    "http://cdn5.thr.com/sites/default/files/2011/06/nicolas_cage_2011_a_p.jpg",
    "http://i0.kym-cdn.com/entries/icons/original/000/006/993/1817.jpg",
    "http://overmental.com/wp-content/uploads/2015/03/nic-cage-face.png",
    "https://i0.wp.com/media2.slashfilm.com/slashfilm/wp/wp-content/images/nicolascage-faceoff-crazy.jpg",
    "https://timenewsfeed.files.wordpress.com/2013/10/screen-shot-2013-10-09-at-4-10-39-pm.png?w=753",
    "https://s.aolcdn.com/hss/storage/midas/627f1d890718ff2c58318a280145a153/203216448/nicholas-cage-con-air.jpg",
    "http://files.gamebanana.com/img/ico/sprays/516c32f08e03d.png",
    "https://pmcdeadline2.files.wordpress.com/2010/08/nicolas_cage.jpg",
    "https://img.buzzfeed.com/buzzfeed-static/static/2014-01/campaign_images/webdr06/7/14/50-reasons-why-nicolas-cage-is-the-greatest-human-1-5571-1389124720-1_big.jpg",
    "http://www.indiewire.com/wp-content/uploads/2015/05/nicolas-cage-1.jpg",
    "http://nerdist.com/wp-content/uploads/2015/12/Nicolas-Cage-Con-Air.jpg",
    "http://images.boomsbeat.com/data/images/full/193575/56000469-jpg.jpg",
    "http://cdn.financebuzz.io/images/2016/02/03/nicholascage1.jpg",
    "https://s3.drafthouse.com/images/made/wild-at-heart-nicolas-cage-wallpapers_758_426_81_s_c1.jpg",
    "http://wallpapersin4k.net/wp-content/uploads/2016/12/Nicolas-Cage-Wallpapers-3.png",
    "http://cdn-static.denofgeek.com/sites/denofgeek/files/nicolas-cage-nicolas-cage-26969958-1974-1300.jpg",
    "http://s3.crackedcdn.com/blogimages/2009/03/cage5.jpg",
    "http://www.hdnetmovies.com/wp-content/uploads/cage1.jpg",
    "http://i1.kym-cdn.com/photos/images/facebook/000/175/835/Cage-intro.jpg",
    "http://akns-images.eonline.com/eol_images/Entire_Site/201506/rs_500x213-150106140225-tumblr_lx7an6a7pT1r4etbjo1_r1_500.gif",
    "https://brightestyoungthings.com/wp-content/uploads/2014/01/nicolas-cage-can-be-anyone-part2-3.jpg",
    "http://healthyceleb.com/wp-content/uploads/2016/01/Nicolas-Cage-shirtless.jpg",
    "http://www.thehunchblog.com/wp-content/uploads/2015/10/Nicolas-Cage-2.png",
    "http://az616578.vo.msecnd.net/files/2016/03/11/635932665636472170-317910928_Cage%20Photo%204.jpg",
    "https://www.famousbirthdays.com/headshots/nicolas-cage-3.jpg",
    "https://www.famousbirthdays.com/headshots/nicolas-cage-5.jpg",
    "http://thesecondtake.com/wp-content/uploads/2013/04/Nicolas-Cage.jpg",
    "http://www.dvdsreleasedates.com/pictures/800/12000/Nicolas-Cage.jpg",
    "http://filmonic.com/wp-content/uploads/2014/03/Nicolas-Cage.jpg",
    "https://pmcdeadline2.files.wordpress.com/2016/02/nicolas-cage.jpg?w=605",
    "http://unrealitymag.com/wp-content/uploads/2009/03/nic-cage-birdhair.jpg",
    "https://i.giphy.com/media/e1XbElGxYqcBa/200_s.gif",
    "http://s.newsweek.com/sites/www.newsweek.com/files/styles/embed-lg/public/2015/09/24/nicolas-cage.jpg",
    "https://www.famousbirthdays.com/faces/cage-nicolas-image.jpg",
    "http://cdn.financebuzz.io/images/2016/02/03/nicolascagepainting18.jpg",
    "http://i.dailymail.co.uk/i/pix/2014/03/05/article-2574191-1C10A89600000578-775_306x423.jpg",
    "http://static.gofugyourself.com/uploads/2015/08/GettyImages-483091042.jpg",
    "https://s-media-cache-ak0.pinimg.com/originals/af/a9/3e/afa93eed58d0e4d014b9e9ef5a11a0fe.png",
    "https://i.giphy.com/media/Za3FFB6aXVAnS/200_s.gif",
    "http://static.srcdn.com/wp-content/uploads/Nicolas-Cage-Vampires-Kiss1.jpg",
    "https://i.ytimg.com/vi/O6uxxek5mbI/maxresdefault.jpg",
)


def main(bot, author_id, message, thread_id, thread_type, **kwargs):
    bot.sendRemoteImage(random.choice(NICKS),
                        message=None,
                        thread_id=thread_id,
                        thread_type=thread_type)
