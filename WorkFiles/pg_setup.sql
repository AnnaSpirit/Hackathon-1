-- 1. Créer le rôle (si ce n’est pas déjà fait)
CREATE ROLE Player_Gamer WITH
    LOGIN
    PASSWORD 'SuperMotDePasseSecu';

-- 2. Révoquer l’accès par défaut aux autres bases
-- (se fait généralement automatiquement, mais tu peux forcer)
REVOKE CONNECT ON DATABASE postgres FROM Player_Gamer;
REVOKE CONNECT ON DATABASE template1 FROM Player_Gamer;

-- 3. Autoriser seulement la connexion à pawn_to_king
GRANT CONNECT ON DATABASE pawn_to_king TO Player_Gamer;

-- 4. Dans pawn_to_king, autoriser l’usage du schéma public
REVOKE ALL ON SCHEMA public FROM Player_Gamer;
GRANT USAGE ON SCHEMA public TO Player_Gamer;

-- 5. Autoriser les opérations sur les tables que tu veux  
--    (ici on donne juste SELECT/INSERT sur toutes les tables existantes)
GRANT SELECT, INSERT, UPDATE, DELETE
    ON ALL TABLES IN SCHEMA public
    TO Player_Gamer;

-- 6. Si tu crées de nouvelles tables plus tard, tu peux automatiser :
ALTER DEFAULT PRIVILEGES IN SCHEMA public
    GRANT SELECT, INSERT, UPDATE, DELETE ON TABLES
    TO Player_Gamer;

-- -- 7. Supprime le rôle player_gamer s’il existe
-- DROP ROLE IF EXISTS player_gamer;