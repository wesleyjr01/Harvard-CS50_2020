function blink()
            {
                let body = document.querySelector('#navbaricon');
                if (body.style.visibility == 'hidden')
                {
                    body.style.visibility = 'visible';
                }
                else
                {
                    body.style.visibility = 'hidden';
                }
            }

// Blink every 500ms
window.setInterval(blink, 500);