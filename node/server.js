const express = require('express');
const path = require('path');
const Proxy = require('https').createServer();

const port = 4002
const app = express();

const ProxyServer = 'http://localhost:' + port;

/**
 * WebSocket Configuration
 */
const io = require('socket.io')(4001, {
    path: '/',

    serveClient: true,
    cors: '*',
    cookie: true,
    pingInterval: 1000,
    pingTimeout: 1000,
    upgradeTimeout: 1000,
    allowUpgrades: true,
    cookie: 'emiga_stream',
    cookiePath: '/',
    cookieHttpOnly: true
});

io.on('connection', function (socket) {
    socket.on('stream', function (data) {
        socket.broadcast.emit('stream', data);
    });
    socket.on('stream-python', function (data) {
        socket.broadcast.emit('stream-python', data)
    })
});

app.listen(port, () => console.log(`\x1b[40m`, `\x1b[32m`,
    `
     _______  __   __  ___   _______  _______ 
    |       ||  |_|  ||   | |       ||   _   |
    |    ___||       ||   | |    ___||  |_|  |
    |   |___ |       ||   | |   | __ |       |
    |    ___||       ||   | |   ||  ||       |
    |   |___ | ||_|| ||   | |   |_| ||   _   |
    |_______||_|   |_||___| |_______||__| |__|
 
    [+] Maintance      : https://github.com/eminmuhammadi/emiga-stream.git
    [+] Server         : http://localhost:${port}
    [+] Socket         : ws://localhost:${port}
    [~] Running Server...
`, `\x1b[0m`));