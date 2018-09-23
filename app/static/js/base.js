 //调用弹出层
    function openlayer(idn1, idn2) {
    	
        $("#" + idn1).fadeIn();
        var vh = $("#" + idn2).height();
        $("#" + idn2).css({ "margin-top": -(vh * 0.5) + "px" });
        $("#" + idn2).addClass("active");
    }

    function closelayer(idn1, idn2) {
        $("#" + idn1).fadeOut();
        $("#" + idn2).removeClass("active");
    }


 //回到顶部
    $("#Backtop").click(function(event) {
        event.preventDefault();
        $('html,body').animate({ scrollTop: '0px' }, 500);
    });
    $(window).scroll(function() {
        if ($(document).scrollTop() > 0) {
            $(".float ul .backtop").addClass('active');
            $(".float").show();
        } else {
            $(".float ul .backtop").removeClass('active');
            $(".float").hide();
        }
    })


      //login
    $("#login").click(function(event) {
        openlayer("layer-bg", "login-layer");
        $(".login-tab li").eq(0).addClass('active').siblings('').removeClass('active');
        $(".login-cons form").eq(0).show().siblings('').hide();
        return false;
    });
    $("#login-close").click(function(event) {
        closelayer("layer-bg", "login-layer");
        return false;
    });
    
    //注册
    $("#reg").click(function(event) {
        openlayer("layer-bg", "login-layer");
        $(".login-tab li").eq(1).addClass('active').siblings('').removeClass('active');
        $(".login-cons form").eq(1).show().siblings('').hide();
        return false;
    });
    $("#login-close").click(function(event) {
        closelayer("layer-bg", "login-layer");
        return false;
    });

    //login 动画
    $(".login-cons .form-item").click(function(event) {
        $(this).find(".form-input").focus().addClass("form-input-focus").siblings('.item-tip').addClass('item-tip-focus');

    });

    //login 切换
    $(".login-tab>li").click(function(event) {

        if ($(".form-input").val() == "") {
            $(".item-tip").removeClass("item-tip-focus");
             $(".form-input").removeClass("form-input-focus");
        }

        var i = $(this).index();
        $(this).addClass("active").siblings("").removeClass("active");
        $(".login-cons form").eq(i).show().siblings().hide();
    });
    //发送验证码
    function invokeSettime(obj) {
        var countdown = 60;
        settime(obj);

        function settime(obj) {
            if (countdown == 0) {
                $(obj).removeClass('disabled')
                $(obj).attr("disabled", false);
                $(obj).text("发送短信验证码");
                countdown = 60;
                return;
            } else {
                $(obj).addClass('disabled')
                $(obj).attr("disabled", true)
                $(obj).text("(" + countdown + ") 秒后从新获取");
                countdown--;
            }
            setTimeout(function() {
                settime(obj)
            }, 1000)
        }
    }

    $(".btn-captcha").click(function(event) {
        new invokeSettime(".btn-captcha");
    });



       //详情页左侧浮动
    var leftImgfixed = function() {

        var detailWrap = $('.detail-wrap'),
            ofTop = detailWrap.offset().top,
            ofHeigth = detailWrap.height() + 220,
            scrollTop = $(".detail-wrap").offset().top + $(".detail-wrap").height() - 220;

        function offShow() {
            var y = $(document).scrollTop();
            if (ofHeigth > $(window).height() && y > scrollTop - 500) {
                $('.detail-content-l-main').addClass("absolute").removeClass("fixed");
                return false;   
            }

            if (y < $('.detail-wrap').offset().top) {
                $('.detail-content-l-main').removeClass('fixed').removeClass("absolute");
            } else {
                $('.detail-content-l-main').addClass('fixed').removeClass("absolute");
            }

        }

        offShow();

        $(window).scroll(offShow);
    }



      //内页发送验证码
    function getyzm (obj) {
        var countdown = 60;
        settime(obj);

        function settime(obj) {
            if (countdown == 0) {
                $(obj).removeClass('disabled')
                $(obj).attr("disabled", false);
                $(obj).text("发送短信验证码");
                countdown = 60;
                return;
            } else {
                $(obj).addClass('disabled')
                $(obj).attr("disabled", true)
                $(obj).text(countdown+ '秒后重发');
                countdown--;
            }
            setTimeout(function() {
                settime(obj)
            }, 1000)
        }
    }



    //会员中心头部下拉
    $(".head-author").click(function(event) {
        $(this).find('.head-author-toggle').slideToggle();
    });