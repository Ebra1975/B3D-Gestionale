# Chiusura Sprint 05

## Obiettivo

Preparare il passaggio operativo verso il mini PC BMAX con Linux Server, mettendo ordine su installazione, backup/ripristino, GitHub e manutenzione.

## Risultato

Lo Sprint 05 non cambia le funzioni del gestionale. Consolida invece le procedure necessarie per usarlo senza dipendere dalla memoria o da passaggi improvvisati.

Sono state rese piu chiare le procedure per:

- installare il gestionale sul BMAX;
- creare backup locali e backup Docker;
- ripristinare una copia di sicurezza;
- aggiornare il server tramite GitHub;
- fare controlli ordinari di manutenzione.

## Funzioni Consegnate

- Board Sprint 05 con obiettivo, ambito e verifiche previste.
- Procedura manutenzione BMAX.
- Aggiornamento installazione BMAX Linux Server.
- Aggiornamento backup e ripristino con attenzione ai volumi Docker.
- Aggiornamento procedura GitHub e routine di aggiornamento.
- Aggiornamento decisioni e approvazioni di progetto.

## Decisione Di Prodotto

Il gestionale deve poter essere mantenuto con procedure semplici e ripetibili.

Per la prima versione il backup automatico completo resta da implementare dopo una prova manuale reale sul BMAX. Prima di affidare dati reali al sistema, backup e ripristino devono essere provati almeno una volta.

## Verifiche

- Controllo documentazione esistente: completato.
- Allineamento procedure con Docker Compose attuale: completato.
- Controllo che lo sprint non introduca modifiche a modello dati o architettura: completato.

## Verifiche Rimaste Manuali

- Installazione reale sul BMAX.
- Verifica LibreOffice PDF sul BMAX.
- Backup manuale reale sul BMAX.
- Ripristino su copia di prova.
- Configurazione eventuale avvio automatico dopo riavvio del mini PC.

## Da Riprendere In Futuro

- Script di backup automatico BMAX.
- Rotazione backup vecchi.
- Controllo automatico spazio disco.
- Notifica esito backup.
- Procedura migrazione dati da Windows SQLite a PostgreSQL, se servira portare dati reali di sviluppo in produzione.
