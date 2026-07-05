import reflex as rx


def carousel_controller_script() -> rx.Component:
    """Injects client-side JS to handle carousel scrolling, highlighting, and and alignment."""
    return rx.script("""
        (function() {
            let scrollTimeout;
            let isUserScrolling = false;

            function initCarousel() {
                const viewport = document.querySelector('.carousel-scroll-viewport');
                if (!viewport) {
                    setTimeout(initCarousel, 50);
                    return;
                }

                viewport.addEventListener('scroll', () => {
                    isUserScrolling = true;
                    highlightMiddleCard(viewport);

                    clearTimeout(scrollTimeout);
                    scrollTimeout = setTimeout(() => {
                        isUserScrolling = false;
                        dispatchMiddleCardSelection(viewport);
                    }, 150);
                }, { passive: true });

                // Watch for active class updates on any card within the viewport
                const observer = new MutationObserver((mutations) => {
                    mutations.forEach(mutation => {
                        if (mutation.type === 'attributes' && mutation.attributeName === 'class') {
                            if (!isUserScrolling) {
                                scrollToActiveCard(viewport);
                            }
                        }
                    });
                });

                observer.observe(viewport, {
                    attributes: true,
                    subtree: true, 
                    attributeFilter: ['class']
                });

                setTimeout(() => {
                    highlightMiddleCard(viewport);
                    scrollToActiveCard(viewport, 'instant'); // Snap instantly on load
                    
                    // Dispatch to ready-bridge input to notify backend
                    const readyBridge = document.getElementById('carousel-ready-bridge');
                    if (readyBridge) {
                        const nativeValueSetter = Object.getOwnPropertyDescriptor(
                            window.HTMLInputElement.prototype, 
                            "value"
                        ).set;
                        nativeValueSetter.call(readyBridge, "ready");
                        readyBridge.dispatchEvent(new Event('input', { bubbles: true }));
                        readyBridge.dispatchEvent(new Event('change', { bubbles: true }));
                    }
                }, 100);
            }

            function highlightMiddleCard(container) {
                const cards = container.querySelectorAll('.event-card');
                if (cards.length === 0) return;
                
                const containerRect = container.getBoundingClientRect();
                const containerCenter = containerRect.left + (containerRect.width / 2);

                let closestCard = null;
                let minDistance = Infinity;

                cards.forEach(card => {
                    const cardRect = card.getBoundingClientRect();
                    const cardCenter = cardRect.left + (cardRect.width / 2);
                    const distance = Math.abs(containerCenter - cardCenter);

                    if (distance < minDistance) {
                        minDistance = distance;
                        closestCard = card;
                    }
                });

                cards.forEach(card => {
                    if (card === closestCard) {
                        card.classList.add('event-card-visually-active');
                    } else {
                        card.classList.remove('event-card-visually-active');
                    }
                });
            }

            function scrollToActiveCard(container, behavior = 'smooth') {
                const activeCard = container.querySelector('.event-card-active');
                if (activeCard) {
                    activeCard.scrollIntoView({
                        behavior: behavior,
                        inline: 'center',
                        block: 'nearest'
                    });
                }
            }

            function dispatchMiddleCardSelection(container) {
                const activeCard = container.querySelector('.event-card-visually-active');
                if (activeCard && activeCard.dataset.id) {
                    const eventId = activeCard.dataset.id;
                    const bridgeInput = document.getElementById('scroll-bridge-input');
                    
                    if (bridgeInput && bridgeInput.value !== eventId) {
                        const nativeValueSetter = Object.getOwnPropertyDescriptor(
                            window.HTMLInputElement.prototype, 
                            "value"
                        ).set;
                        
                        nativeValueSetter.call(bridgeInput, eventId);
                        bridgeInput.dispatchEvent(new Event('input', { bubbles: true }));
                        bridgeInput.dispatchEvent(new Event('change', { bubbles: true }));
                    }
                }
            }

            if (document.readyState === 'complete' || document.readyState === 'interactive') {
                initCarousel();
            } else {
                document.addEventListener('DOMContentLoaded', initCarousel);
            }
        })();
    """)
