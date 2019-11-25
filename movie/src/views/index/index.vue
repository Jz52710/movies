<template>
    <div class="index-box">
        <el-container>
            <el-main style="padding: 0!important;">
                <el-header>
                    <Header></Header>
                </el-header>
                <!--轮播-->
                <el-carousel>
                    <el-carousel-item v-for="item in 4" :key="item"></el-carousel-item>
                </el-carousel>
                <el-container style="width: 1180px;margin: 0 auto;padding: 40px 0 30px;height: auto">
                    <!--左推荐-->
                    <el-aside width="860px">
                        <el-row :span="24" style="background: #f9f9f9">
                            <el-col :span="16">
                                <el-row :span="24">
                                    <el-menu :default-active="activeIndex" class="el-menu-demo" mode="horizontal" @select="handleSelect" background-color="#F9F9F9" active-text-color="#409EFF" style="display:flex;">
                                        <el-menu-item index="1">
                                            <router-link :to="{name:'intelligent'}" tag="div" style="width: 96px;">
                                                智能推荐
                                            </router-link>
                                        </el-menu-item>
                                        <el-menu-item index="2">
                                            <router-link :to="{name:'classify'}" tag="div" style="width: 96px;">
                                                电影分类
                                            </router-link>
                                        </el-menu-item>
                                        <el-menu-item index="3">
                                            <router-link :to="{name:'ranking'}" tag="div" style="width: 96px;">
                                                最热排行
                                            </router-link>
                                        </el-menu-item>
                                        <el-menu-item index="4">
                                            <router-link :to="{name:'hot'}" tag="div" style="width: 96px;">
                                                正在热映
                                            </router-link>
                                        </el-menu-item>
                                    </el-menu>
                                </el-row>
                            </el-col>
                        </el-row>
                        <el-row>
                            <router-view :mysqlData="mysqlData.slice((currentPage-1)*pageSize,currentPage*pageSize)" :total="total" :currentPage="currentPage" :pageSize="pageSize" v-on:currentPage="successz($event)"></router-view>
                        </el-row>
                    </el-aside>
                    <!--右推荐-->
                    <el-main style="width: 300px!important;padding: 0!important;margin-left: 20px">
                        <el-card class="box-card">
                            <div slot="header" class="clearfix">
                                <span>精彩点评</span>
                            </div>
                            <div class="dp-box">
                                <span>#《小丑》一个精神病患者从受害者到恶魔的自白#</span>
                                <p>小丑看到生活中的希望一个个破灭：丢掉工作，成为最不好笑的脱口秀艺人，他不是富翁的私生子，邻居女子并不如他所想。然后他看到韦恩们是多么冷酷无情，毫不关心他的死活：社会救助项目被砍掉，费尽心机见到韦恩只得到一记老拳，然后韦恩却在电视上一直宣传他的慈善晚宴和竞选计划。失业工人看到的也是希望的破灭：制造业的工作越来越少，整个本地社区越来越衰败。有人建议他们重回学校提高教育程度，但是对于一个高中毕业、离开校园几十年的人，那是难于登天的事情；何况学费很贵，他们根本负担不起。然后他们看到造成金融危机的大银行拿到政府的大笔救助，他们看到华尔街的人谁也没进监狱，他们看到高管们短短几年以后继续拿天文数字的薪酬。</p>
                            </div>
                            <div class="dp-box">
                                <span>#秒速五厘米，灵魂飘落的速度#</span>
                                <p>当你走在熙熙攘攘的街头，忽然，一张似曾相识的脸出现在眼帘之中。未及细看，那身影已翩然而过。当你回头，茫茫人海里已无处寻觅，而刚才的邂逅，竟不知是真实存在，还是脑海中的虚幻。猛然间，那个曾经才下眉头却上心头的名字，就这样再次萦绕不去了。</p>
                            </div>
                            <div class="dp-box">
                                <span>#谎言终究是谎言#</span>
                                <p>当人懂得和体制交换的时候，他们可以将真实的自己和盘托出，因为他们的眼里，在与体制作出等价交换以前，真实对他们什么也不是。而一直被欺瞒的楚门在真相大白的一刻选择了决裂，虽然导演最后苦苦规劝，声情并茂，告诉楚门外面的世界和他给楚门的一样虚假，一样有谎言，可是楚门还是决然而去，寻找没有“导演”的生活。结局虽然快慰人心，可是看过之后还是不免陷入悲观，也许楚门得到只是又一个圈套，不同的是他只是又回到了欺骗的起点，就像是他刚刚出生一样。怪不得朋友看过之后不觉得释然，反而失落，并对楚门的世界产生了深深地向往……</p>
                            </div>
                            <div class="dp-box">
                                <span>#那些无声的羁绊，那些有声的家#</span>
                                <p>这部戏太精彩，再看一次，几乎没有任何一句废话与一刻停歇，但是在众多情节中，我还是两次被看不到的烟花所打动了，一家人在矮矮的屋檐下，只能听到声响的烟花，就像这个无声的家庭一样，在社会的最底层，没有任何声响。其实我们都有意无意地忽视了社会的某些人，甚至我们的媒体与gov也不愿意去在意这些无声的群体。但是他们却确实存在，哪怕他们看不到烟花，可是他们的世界也会隆隆作响。</p>
                            </div>
                            <div class="dp-box">
                                <span>#合理的戏说不叫胡说，创新的改编不算乱编#</span>
                                <p>很多人喜欢《哪吒》，可能还是从电影中看到了自己身上的影子，其实我们每个人都是哪吒，怀着一颗赤子之心来到这世间，却会因为旁人的目光、家人的过度保护、遭逢的恶意而改变自己的初心，甚至觉得自己与这个社会格格不入，但内心深处，还是善良、单纯的本质。</p>
                            </div>
                            <div class="dp-box">
                                <span>#你保护世界，我保护你#</span>
                                <p>面对坠楼，他们忙着拍照发微信，只有陈念为她盖上衣服。 面对欺凌，他们假装没看见，只有陈念选择报警。 因为盖衣服，她成了下一个被欺负的人； 因为报警，她遭到疯狂报复。 袖手旁观的人平安无事，制止恶行却受到牵连。 被欺负了没人管，欺负你的人死了马上就管了。 受到伤害无法得到保护，犯了罪绝不让你少判一天。 当初不重视你的遭遇，不了了之； 如今却想尽快结案，让你接受法律制裁。 人人都说可以帮你，其实没有人能帮你。</p>
                            </div>
                        </el-card>
                    </el-main>
                </el-container>
                <el-footer>
                    <el-row :span="24" style="font-size: 12px">
                        <span style="margin-right: 20px">Copyright © 2011-2018</span>
                        <span style="margin-right: 20px">
                            <a href="/" style="text-decoration: none;color: #cccccc">爱电影</a>
                        </span>
                        <span style="margin-right: 10px">京ICP备14003808号-5</span>
                        <span class="tu-box">
                            <img src="../../assets/ba-icon.png" alt="">
                            <span>京公网安备11010102002904号</span>
                        </span>
                    </el-row>
                </el-footer>
            </el-main>
        </el-container>
    </div>
</template>

<script>
    // @ is an alias to /src
    // import HelloWorld from '@/components/HelloWorld.vue'
    import Header from '@/components/header/header.vue'

    export default {
        name: 'index',
        components: {
            // HelloWorld
            Header
        },
        data(){
            return {
                total:200,
                currentPage:1,
                pageSize:10,
                activeIndex: '1',
                mysqlData:[],
            }
        },
        methods: {
            handleSelect() {
            },
            successz(val){
                this.currentPage=val;
                this.pageSize=10;
                this.total=200;
                // alert(val)
            }
        },
        mounted(){
            this.$axios.get('/api/information').then((data)=>{
                // alert(data.data.data[0].score);
                this.mysqlData = data.data.data
            }).catch((error)=>{
                alert(error)
            })
        },

    }
</script>
<style>
    .index-box{
        width: 100%;
        height: 100%;
    }
    .el-container{
        width: 100%;
        height: 100%;
        /*background: #555;*/
    }
    .el-header{
        background-color: rgb(249, 249, 249);
        box-shadow: rgba(0, 0, 0, 0.1) 0px 1px 4px;
        opacity: 0.97;
        color: #333;
        text-align: center;
        line-height: 60px;
        padding: 0 24px!important;
        /*position: fixed;*/
        z-index: 10;
        width: 100%;
    }
    .el-main {
        background-color: #F1F1F1;
        color: #333;
        text-align: center;
        /*line-height: 160px;*/
        /*padding: 0 24px!important;*/
    }
    .left-box{
        font-weight: 600;
        font-size: 24px;
    }

    /*轮播*/
    .el-carousel__item h3 {
        color: #475669;
        font-size: 18px;
        opacity: 0.75;
        line-height: 300px;
        margin: 0;
    }
    .el-carousel__item:nth-child(2n) {
        background: url("../../assets/lb4.jpg");
        background-size: cover;
    }

    .el-carousel__item:nth-child(2n+1) {
        background: url("../../assets/lb3.jpg");
        background-size: cover;
    }
    .el-carousel__item:nth-child(3) {
        background: url("../../assets/lb2.jpg");
        background-size: cover;
    }
    .el-carousel__item:nth-child(4) {
        background: url("../../assets/lb1.jpg");
        background-size: cover;
    }
    .el-carousel--horizontal{
        height: 500px;
    }
    .el-carousel__container{
        height: 500px;
    }
    .table-box .el-breadcrumb__item span{
        font-weight: 400;
    }
    .el-footer {
        background-color: #222222;
        color: #cccccc;
        text-align: center;
        line-height: 60px;
        height: 60px!important;
    }
    .tu-box{
        position: relative;
    }
    .el-footer .tu-box img{
        position: absolute;
        top: -4px;
    }
    .el-footer .tu-box span{
        margin-left: 20px;
    }
    /*卡片*/
    .clearfix{
        text-align: left;
        font-weight: 600;
        border-left: 4px solid #2689FF;
        padding-left: 8px;
    }
    .dp-box{
        color: #333;
        text-align: left;
        margin-bottom: 10px;
    }
    .dp-box span{
        font-weight: bold;
        font-size: 14px;
    }
    .dp-box p{
        background-color: rgb(241, 241, 241);
        border-radius: 10px;
        font-size: 12px;
        color: #666666;
        padding: 10px;
        margin-top: 10px;
    }
    .box-card{
        padding: 0 20px;
    }
    .el-card__body{
        padding: 0!important;
    }
    .el-card__header{
        padding: 18px 0!important;
    }
</style>
