const express = require("express"); //express: framework para node js
const app = express(); //esta constante inicializa express
const cors = require("cors"); //medida de seguridad para navegadores
const mercadopago = require("mercadopago");
const path = require("path"); //Direccion a los directorios necesarios para arrancar el servidor

// REPLACE WITH YOUR ACCESS TOKEN AVAILABLE IN: https://developers.mercadopago.com/panel
mercadopago.configure({
    access_token: "<ACCESS_TOKEN>",
});

app.use(express.urlencoded({ extended: false }));
app.use(express.json());

app.use(express.static(path.join(__dirname, "../client")));
app.use(cors());

app.get("/", function () {
    res.sendFile(path.resolve(__dirname, "..", "client", "index.html"));
});

app.post("/create_preference", (req, res) => {

    let preference = {
        items: [
            {
                title: req.body.description,
                unit_price: Number(req.body.price),
                quantity: Number(req.body.quantity),
            }
        ],
        back_urls: {
            "success": "http://localhost:8080", //si la compra se realizó con éxito, redirige al servidor localhost:8080
            "failure": "http://localhost:8080", //si falla, volvemos a la página principal
            "pending": "" //si está pendiente queda en blanco, NO lo usaremos
        },
        auto_return: "approved", //te retorna al servidor
    };

    mercadopago.preferences.create(preference)
        .then(function (response) {
            res.json({
                id: response.body.id
            });
        }).catch(function (error) {
        console.log(error);
    });
});

//CONFIGURACIONES AVANZADAS SOBRE EL ESTADO DEL PAGO -> NO LAS USAREMOS
app.get('/feedback', function (req, res) {
    res.json({
        Payment: req.query.payment_id,
        Status: req.query.status,
        MerchantOrder: req.query.merchant_order_id
    });
});

app.listen(8080, () => {
    console.log("The server is now running on Port 8080");
});
