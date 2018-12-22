
var app = new Vue ({
    el: "#app",
    data: {
        message: "Hello Vue"
    }
});

app.message = "Hello IPCalculator";


var calc = new Vue ({
    el: "#calc",
    data: {
        ip_addr: "",
        net_mask: "",
        info: ""
    },
    methods: {
        calcIP: function () {
            axios
                .get("/ip-detail", {
                    params: {ip: this.ip_addr, mask: this.net_mask}
                })
                .then(response => (this.info = response.data));
        }
    }
});

